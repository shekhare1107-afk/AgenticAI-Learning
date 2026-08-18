from fastapi import APIRouter

from app.agent.agent import Agent

router = APIRouter()


@router.get("/chat")
def chat(
    message: str,
    provider: str = "gemini",
):
    agent = Agent(provider=provider)

    return {
        "provider": provider,
        "response": agent.run(message),
    }