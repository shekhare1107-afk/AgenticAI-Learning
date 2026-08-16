from fastapi import APIRouter
from app.services.ai_service import Agent

router = APIRouter()
agent = Agent()


@router.get("/chat")
def chat(message: str):

    return {
        "response": agent.run(message)
    }