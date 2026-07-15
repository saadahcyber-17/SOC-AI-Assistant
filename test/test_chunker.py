import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents

documents = load_documents()

chunks = chunk_documents(documents)

print(chunks)