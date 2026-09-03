import logging

from fastapi import APIRouter, HTTPException

from app.agent.agent import Agent
from app.core.exceptions import AgentError


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/chat")
def chat(
    message: str,
    provider: str = "gemini",
):
    try:
        logger.info(
            "Chat request received. Provider: %s",
            provider
        )

        agent = Agent(provider=provider)

        response = agent.run(message)

        logger.info(
            "Chat request completed successfully. Provider: %s",
            provider
        )

        return {
            "success": True,
            "provider": provider,
            "response": response,
        }

    except AgentError:
        # Let the global exception handler handle
        # all custom Agent exceptions.
        raise

    except ValueError as error:
        logger.warning(
            "Chat request validation error. Provider: %s. Error: %s",
            provider,
            str(error),
        )

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception:
        logger.exception(
            "Unexpected error while processing chat request. Provider: %s",
            provider,
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "Something went wrong while processing your request. "
                "Please try again."
            ),
        )