import requests


OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"

MODEL_NAME = "nomic-embed-text"


def generate_embedding(text: str):

    response = requests.post(
        OLLAMA_EMBED_URL,
        json={
            "model": MODEL_NAME,
            "prompt": text
        }
    )

    result = response.json()

    return result["embedding"]