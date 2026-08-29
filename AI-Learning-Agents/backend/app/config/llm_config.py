import os

from dotenv import load_dotenv


load_dotenv()


class LLMProviderConfig:

    def __init__(
        self,
        name: str,
        enabled: bool,
        api_key: str | None,
    ):
        self.name = name
        self.enabled = enabled
        self.api_key = api_key


def _get_bool(value: str | None) -> bool:
    return value is not None and value.lower() == "true"


OPENAI_CONFIG = LLMProviderConfig(
    name="openai",
    enabled=_get_bool(os.getenv("OPENAI_ENABLED")),
    api_key=os.getenv("OPENAI_API_KEY"),
)


ANTHROPIC_CONFIG = LLMProviderConfig(
    name="anthropic",
    enabled=_get_bool(os.getenv("ANTHROPIC_ENABLED")),
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)


GOOGLE_CONFIG = LLMProviderConfig(
    name="google",
    enabled=_get_bool(os.getenv("GOOGLE_ENABLED")),
    api_key=os.getenv("GOOGLE_API_KEY"),
)