from app.services.llm_service import LLMService
from app.services.mock_llm import MockLLM
from app.services.openai_service import OpenAIService
from app.services.claude_service import ClaudeService
from app.services.gemini_service import GeminiService

from app.config.llm_config import (
    OPENAI_CONFIG,
    ANTHROPIC_CONFIG,
    GOOGLE_CONFIG,
)


class LLMFactory:

    @staticmethod
    def create(provider: str) -> LLMService:

        provider = provider.lower()

        if provider == "mock":
            return MockLLM()

        if provider == "openai":
            if not OPENAI_CONFIG.enabled:
                raise ValueError("OpenAI provider is disabled.")

            if not OPENAI_CONFIG.api_key:
                raise ValueError("OpenAI API key is not configured.")

            return OpenAIService()

        if provider == "anthropic":
            if not ANTHROPIC_CONFIG.enabled:
                raise ValueError("Claude provider is disabled.")

            if not ANTHROPIC_CONFIG.api_key:
                raise ValueError("Claude API key is not configured.")

            return ClaudeService()

        if provider == "google":
            if not GOOGLE_CONFIG.enabled:
                raise ValueError("Gemini provider is disabled.")

            if not GOOGLE_CONFIG.api_key:
                raise ValueError("Gemini API key is not configured.")

            return GeminiService()

        raise ValueError(f"Unsupported LLM provider: {provider}")