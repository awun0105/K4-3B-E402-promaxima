import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from env_loader import load_lab_env
from providers import make_provider
from tools import load_tool_declarations, to_openai_tools
from chat import run_model_tool_loop

# Load env variables (API keys)
load_lab_env(ROOT)

ARTIFACTS_DIR = ROOT / "artifacts"
SYSTEM_PROMPT = (ARTIFACTS_DIR / "system_prompt.md").read_text(encoding="utf-8")
TOOL_DECLARATIONS = load_tool_declarations(ARTIFACTS_DIR / "tools.yaml")
OPENAI_TOOLS = to_openai_tools(TOOL_DECLARATIONS)

# Use Gemini by default since it's fast and we might have Google keys loaded in this environment
PROVIDER = make_provider("openrouter")
MODEL = getattr(PROVIDER, "default_model", None)

class ChatAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                user_msg = data.get('message', '')
                bot_type = data.get('bot_type', 'new')
                
                print(f"Received request: {user_msg} for bot type: {bot_type}")
                
                if bot_type == "old":
                    # Bot Cũ doesn't have tools, it just guesses
                    sys_prompt = "You are a helpful assistant. You must answer the user's question directly. Do not ask for clarification. Do not use tools. Just guess an answer if you don't know."
                    messages = [
                        {"role": "system", "content": sys_prompt},
                        {"role": "user", "content": user_msg}
                    ]
                    # No tools for old bot
                    result = run_model_tool_loop(
                        provider=PROVIDER,
                        messages=messages,
                        tools=[],
                        model=MODEL,
                        max_tool_rounds=1
                    )
                else:
                    # Bot Mới uses full RAG tools and system prompt
                    messages = [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_msg}
                    ]
                    result = run_model_tool_loop(
                        provider=PROVIDER,
                        messages=messages,
                        tools=OPENAI_TOOLS,
                        model=MODEL,
                        max_tool_rounds=4
                    )
                
                # Format response nicely
                assistant_text = result.get("assistant_text", "")
                
                # If there were tool events, append them at the bottom as mock Discord code block
                tool_events = result.get("tool_events", [])
                if tool_events:
                    tool_logs = "\\n".join([f"[Action: {event['tool']}(...)]" for event in tool_events])
                    assistant_text += f"<br><br><span class='text-xs text-[#249858] font-mono'>{tool_logs}</span>"

                response_data = {
                    "response": assistant_text,
                    "status": result.get("status", "success"),
                    "tool_events": tool_events,
                    "rounds": result.get("rounds", [])
                }
                
                self._set_headers()
                self.wfile.write(json.dumps(response_data).encode('utf-8'))
                
            except Exception as e:
                import traceback
                traceback.print_exc()
                self._set_headers(500)
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        elif self.path == '/run-eval':
            import subprocess
            try:
                print("Running automated evaluation via UI request...")
                # Run the eval script (Base suite 24 cases for safe API timeout)
                process = subprocess.Popen(
                    ["python", "run_eval.py", "--provider", "openrouter", "--suite", "base", "--version", "v3", "--eval-cases", "../eval/eval_base_discord.json"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    cwd=str(ROOT)
                )
                output, _ = process.communicate(timeout=180)
                
                # Parse output to make it look nice
                lines = output.split('\n')
                summary = [line for line in lines if "PASS" in line or "FAIL" in line or "Accuracy" in line or "Summary" in line or "total" in line or "passed" in line]
                
                self._set_headers()
                self.wfile.write(json.dumps({"status": "success", "output": output, "summary": "\n".join(summary[-15:])}).encode('utf-8'))
            except Exception as e:
                self._set_headers(500)
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(port=8081):
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, ChatAPIHandler)
    print(f"Starting Backend API server on port {port} using {PROVIDER.__class__.__name__}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
