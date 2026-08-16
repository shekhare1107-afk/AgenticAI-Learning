from app.services.llm_factory import LLMFactory
from app.services.llm_service import LLMService
from app.tools.registry import ToolRegistry


class Agent:

    def __init__(
        self,
        provider: str = "mock",
        llm: LLMService | None = None,
    ):
        self.llm = llm or LLMFactory.create(provider)
        self.tool_registry = ToolRegistry()

    def run(self, message: str):

        decision = self.llm.decide(message)

        if decision["type"] == "final_response":
            return decision["content"]

        if decision["type"] == "tool_call":

            tool_name = decision["tool"]
            arguments = decision["arguments"]

            tool = self.tool_registry.get_tool(tool_name)

            if tool is None:
                return f"Tool '{tool_name}' is not available."

            try:
                result = tool.function(**arguments)

                return f"The answer is {result}"

            except ValueError as error:
                return f"Tool error: {error}"

        return "I could not understand the request."