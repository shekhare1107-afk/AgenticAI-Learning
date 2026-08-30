from app.services.llm_factory import LLMFactory
from app.services.llm_service import LLMService
from app.tools.registry import ToolRegistry
import logging

logger = logging.getLogger(__name__)

class Agent:

    def __init__(
        self,
        provider: str = "mock",
        llm: LLMService | None = None,
    ):
        self.llm = llm or LLMFactory.create(provider)
        self.tool_registry = ToolRegistry()

    def run(self, message: str):

        context = [
            {
                "type": "user_message",
                "content": message,
            }
        ]

        max_iterations = 5

        for iteration in range(max_iterations):

            logger.info("Agent iteration %s/%s started.",iteration + 1,max_iterations)


            decision = self.llm.decide(context)

            logger.info("Agent decision %s/%s: %s",iteration + 1,max_iterations,decision["type"])

            if decision["type"] == "final_response":
                return decision["content"]

            if decision["type"] == "tool_call":

                tool_name = decision["tool"]
                arguments = decision["arguments"]

                logger.info(
                    "Executing tool '%s' with arguments: %s",
                    tool_name,
                    arguments,
                )

                tool = self.tool_registry.get_tool(tool_name)

                if tool is None:
                    return f"Tool '{tool_name}' is not available."

                try:
                    result = tool.function(**arguments)

                    logger.info(
                        "Tool '%s' executed successfully. Result: %s",
                        tool_name,
                        result,
                        )

                    context.append(
                        {
                            "type": "tool_result",
                            "tool": tool_name,
                            "result": result,
                        }
                    )

                    # Do not return here.
                    # The loop should continue and ask the LLM again.
                    continue

                except ValueError as error:

                    logger.warning(
                        "Tool '%s' failed with validation error. Error: %s",
                        tool_name,
                        str(error),
                        )

                    continue

                except Exception:

                    logger.exception(
                        "Unexpected error while executing tool '%s'.",
                        tool_name,
                        )
              
                    return "An unexpected error occurred while executing the tool."

        logger.warning(
            "Agent stopped after reaching maximum iterations: %s",
            max_iterations,
            )

        return (
            "I could not complete the request within the allowed number "
            "of execution steps."
        )