import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.rag.loader import load_documents

documents = load_documents()

print(documents)