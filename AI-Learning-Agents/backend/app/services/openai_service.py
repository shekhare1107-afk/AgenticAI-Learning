from app.services.llm_service import LLMService
from app.config.llm_config import OPENAI_CONFIG


class OpenAIService(LLMService):

    def __init__(self):
        self.config = OPENAI_CONFIG

    def decide(self, message: str) -> dict:
        raise NotImplementedError(
            "OpenAI integration will be implemented next."
        )