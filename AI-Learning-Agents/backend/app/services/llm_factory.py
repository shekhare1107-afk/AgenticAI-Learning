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

from app.core.exceptions import ProviderError


class LLMFactory:

    @staticmethod
    def create(provider: str) -> LLMService:

        provider = provider.lower()

        if provider == "mock":
            return MockLLM()

        if provider == "openai":

            if not OPENAI_CONFIG.enabled:
                raise ProviderError(
                    message="OpenAI provider is currently disabled.",
                    status_code=503,
                    error_code="PROVIDER_DISABLED",
                )

            if not OPENAI_CONFIG.api_key:
                raise ProviderError(
                    message="OpenAI API key is not configured.",
                    status_code=500,
                    error_code="API_KEY_MISSING",
                )

            return OpenAIService()

        if provider in ["anthropic", "claude"]:

            if not ANTHROPIC_CONFIG.enabled:
                raise ProviderError(
                    message="Claude provider is currently disabled.",
                    status_code=503,
                    error_code="PROVIDER_DISABLED",
                )

            if not ANTHROPIC_CONFIG.api_key:
                raise ProviderError(
                    message="Claude API key is not configured.",
                    status_code=500,
                    error_code="API_KEY_MISSING",
                )

            return ClaudeService()

        if provider in ["google", "gemini"]:

            if not GOOGLE_CONFIG.enabled:
                raise ProviderError(
                    message="Gemini provider is currently disabled.",
                    status_code=503,
                    error_code="PROVIDER_DISABLED",
                )

            if not GOOGLE_CONFIG.api_key:
                raise ProviderError(
                    message="Gemini API key is not configured.",
                    status_code=500,
                    error_code="API_KEY_MISSING",
                )

            return GeminiService()

        raise ProviderError(
            message=f"Unsupported LLM provider: {provider}",
            status_code=400,
            error_code="UNSUPPORTED_PROVIDER",
        )