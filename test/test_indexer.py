import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.rag.indexer import build_index

build_index()