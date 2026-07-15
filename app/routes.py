from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse
from app.rag.rag_service import ask_rag

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = ask_rag(request.question)

    return ChatResponse(
        answer=answer
    )