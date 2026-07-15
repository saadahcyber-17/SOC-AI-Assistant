def chunk_documents(documents, chunk_size=300):

    chunks = []

    for document in documents:

        text = document["content"]

        filename = document["filename"]

        for i in range(0, len(text), chunk_size):

            chunk = text[i:i + chunk_size]

            chunks.append(
                {
                    "filename": filename,
                    "content": chunk
                }
            )

    return chunks