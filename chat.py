from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CODEBASE_DIR = ROOT / "codebase"
if str(CODEBASE_DIR) not in sys.path:
    sys.path.insert(0, str(CODEBASE_DIR))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from codebase.chat import main

if __name__ == "__main__":
    main()
