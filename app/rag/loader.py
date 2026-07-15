from pathlib import Path


DATA_FOLDER = Path("data")


def load_documents():

    documents = []

    for file in DATA_FOLDER.glob("*.txt"):

        with open(file, "r", encoding="utf-8") as f:

            text = f.read()

        documents.append(
            {
                "filename": file.name,
                "content": text
            }
        )

    return documents