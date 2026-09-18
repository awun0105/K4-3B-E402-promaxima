.PHONY: install run-backend run-ui run-cli eval-base eval-adv eval-group eval-all

# Cài đặt các thư viện cần thiết
install:
	pip install -r codebase/requirements.txt

# Chạy Backend Server cho Bot mới (mặc định port 8081)
run-backend:
	cd codebase && python server.py

# Mở UI (Web App giả lập Discord)
run-ui:
	@echo "Đang khởi động UI server trên cổng 8082..."
	@echo "👉 Hãy click vào link này: http://localhost:8082/codebase/mock.html"
	python -m http.server 8082

# Chat trực tiếp trên Terminal (không cần UI)
run-cli:
	cd codebase && python chat.py --provider openrouter --version v3

# Chạy cả Backend và UI cùng lúc (tiện nhất)
start:
	@echo "🧹 Đang dọn dẹp (kill) các tiến trình cũ trên cổng 8081 và 8082..."
	@fuser -k 8081/tcp 2>/dev/null || true
	@fuser -k 8082/tcp 2>/dev/null || true
	@echo "Đang khởi động Backend (port 8081) và UI Server (port 8082)..."
	@kill -9 $$(lsof -t -i:8081 -i:8082) 2>/dev/null || true
	@cd codebase && python server.py &
	@python -m http.server 8082 &
	@echo "✅ Đã bật xong cả hai!"
	@echo "👉 Bạn hãy truy cập link này: http://localhost:8082/codebase/mock.html"

# Chạy kiểm thử (Evaluation) cho các bộ case
eval-base:
	cd codebase && python run_eval.py --provider openrouter --suite base --version v3

eval-adv:
	cd codebase && python run_eval.py --provider openrouter --suite adversarial --version v3

eval-group:
	cd codebase && python run_eval.py --provider openrouter --suite group --version v3

# Chạy toàn bộ các bộ kiểm thử
eval-all: eval-base eval-adv eval-group
