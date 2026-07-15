import chromadb

from app.rag.embeddings import generate_embedding

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("soc_documents")


def retrieve(query, top_k=3):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]