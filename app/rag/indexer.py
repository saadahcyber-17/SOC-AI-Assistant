from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.embeddings import generate_embedding
from app.rag.vector_store import store_chunks


def build_index():

    documents = load_documents()

    chunks = chunk_documents(documents)

    for chunk in chunks:

        chunk["embedding"] = generate_embedding(
            chunk["content"]
        )

    store_chunks(chunks)

    print("Knowledge Base Indexed Successfully!")