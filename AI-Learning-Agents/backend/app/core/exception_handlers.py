import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AgentError


logger = logging.getLogger(__name__)


async def agent_error_handler(
    request: Request,
    exc: AgentError,
):
    logger.error(
        "Agent error occurred. "
        "Error ID: %s | "
        "Error Code: %s | "
        "Path: %s | "
        "Message: %s",
        exc.error_id,
        exc.error_code,
        request.url.path,
        exc.message,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "error_id": exc.error_id,
                "error_code": exc.error_code,
                "message": exc.message,
            },
        },
    )