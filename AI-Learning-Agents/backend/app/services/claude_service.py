from app.services.llm_service import LLMService
from app.config.llm_config import ANTHROPIC_CONFIG


class ClaudeService(LLMService):

    def __init__(self):
        self.config = ANTHROPIC_CONFIG

    def decide(self, message: str) -> dict:
        raise NotImplementedError(
            "Claude integration has not been implemented yet."
        )