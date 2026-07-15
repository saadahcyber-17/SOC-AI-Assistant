import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="soc_documents"
)


def store_chunks(chunks):

    ids = []

    documents = []

    embeddings = []

    metadatas = []

    for index, chunk in enumerate(chunks):

        ids.append(str(index))

        documents.append(chunk["content"])

        embeddings.append(chunk["embedding"])

        metadatas.append(
            {
                "filename": chunk["filename"]
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )