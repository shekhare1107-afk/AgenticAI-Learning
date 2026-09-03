import logging

from app.core.exceptions import ToolExecutionError
from app.services.llm_factory import LLMFactory
from app.services.llm_service import LLMService
from app.tools.registry import ToolRegistry


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

            logger.info(
                "Agent iteration %s/%s started.",
                iteration + 1,
                max_iterations,
            )

            decision = self.llm.decide(context)

            logger.info(
                "Agent decision %s/%s: %s",
                iteration + 1,
                max_iterations,
                decision["type"],
            )

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

                    logger.error(
                        "Requested tool '%s' is not available.",
                        tool_name,
                    )

                    raise ToolExecutionError(
                        message=f"Tool '{tool_name}' is not available.",
                        status_code=400,
                        error_code="TOOL_NOT_FOUND",
                    )

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

                    # Continue the agent loop.
                    # The LLM receives the tool result and decides
                    # whether another tool is required or a final
                    # response can be returned.
                    continue

                except ValueError as error:

                    logger.exception(
                        "Tool '%s' execution failed with validation error. "
                        "Arguments: %s",
                        tool_name,
                        arguments,
                    )

                    raise ToolExecutionError(
                        message=f"Invalid input while executing tool '{tool_name}'.",
                        status_code=400,
                        error_code="TOOL_VALIDATION_ERROR",
                    ) from error

                except Exception as error:

                    logger.exception(
                        "Unexpected error while executing tool '%s'. "
                        "Arguments: %s",
                        tool_name,
                        arguments,
                    )

                    raise ToolExecutionError(
                        message=f"Failed to execute tool '{tool_name}'.",
                        status_code=500,
                        error_code="TOOL_EXECUTION_ERROR",
                    ) from error

        logger.warning(
            "Agent stopped after reaching maximum iterations: %s",
            max_iterations,
        )

        return (
            "I could not complete the request within the allowed number "
            "of execution steps."
        )