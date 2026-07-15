import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.rag.embeddings import generate_embedding

text = "Event ID 4625 indicates failed logon attempts."

embedding = generate_embedding(text)

print(type(embedding))

print(len(embedding))

print(embedding[:10])