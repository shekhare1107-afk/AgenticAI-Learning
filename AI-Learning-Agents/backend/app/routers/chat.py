from fastapi import APIRouter

from app.agent.agent import Agent
from app.services.gemini_service import GeminiService

router = APIRouter()

agent = Agent(
    llm=GeminiService()
)


@router.get("/chat")
def chat(message: str):

    return {
        "response": agent.run(message)
    }