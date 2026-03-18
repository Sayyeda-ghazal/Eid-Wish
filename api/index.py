import sys
from pathlib import Path

# Ensure project root is on sys.path so we can import app.py
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import app

# Vercel looks for a module-level "app" object
