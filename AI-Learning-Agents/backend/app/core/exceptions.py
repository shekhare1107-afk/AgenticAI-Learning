import uuid


class AgentError(Exception):
    """Base exception for all AI Agent errors."""

    def __init__(
        self,
        message: str,
        status_code: int = 500,
        error_code: str = "AGENT_ERROR",
        error_id: str | None = None,
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code

        # Unique ID for tracking this specific error
        self.error_id = error_id or str(uuid.uuid4())

        super().__init__(message)


class ProviderError(AgentError):
    """Raised when there is an LLM provider problem."""

    pass


class ToolExecutionError(AgentError):
    """Raised when a tool execution fails."""

    pass