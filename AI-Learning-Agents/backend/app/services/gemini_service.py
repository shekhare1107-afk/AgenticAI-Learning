from app.services.llm_service import LLMService
from app.config.llm_config import GOOGLE_CONFIG


class GeminiService(LLMService):

    def __init__(self):
        self.config = GOOGLE_CONFIG

    def decide(self, message: str) -> dict:
        raise NotImplementedError(
            "Gemini integration has not been implemented yet."
        )