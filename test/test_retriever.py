import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.rag.retriever import retrieve

chunks = retrieve(
    "What is Event ID 4625?"
)

print(chunks)