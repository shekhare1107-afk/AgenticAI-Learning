from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.logger import setup_logging

from app.routers.health import router as health_router
from app.routers.chat import router as chat_router

from app.core.exceptions import AgentError
from app.core.exception_handlers import agent_error_handler

setup_logging()

app = FastAPI(
    title="AI Learning Agent",
    version="1.0.0"
)

# Register global Agent exception handler
app.add_exception_handler(
    AgentError,
    agent_error_handler,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
        "http://127.0.0.1:5173",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(chat_router)