from app.rag.retriever import retrieve
from app.rag.prompt_builder import build_prompt
from app.ollama_client import generate_response


def ask_rag(question):

    documents = retrieve(question)

    prompt = build_prompt(
        question,
        documents
    )

    answer = generate_response(prompt)

    return answer