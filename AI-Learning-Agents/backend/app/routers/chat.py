from fastapi import APIRouter
from app.services.ai_service import AIService

router = APIRouter()

ai_service = AIService()


@router.get("/chat")
def chat(message: str):

    return {
        "response": ai_service.chat(message)
    }