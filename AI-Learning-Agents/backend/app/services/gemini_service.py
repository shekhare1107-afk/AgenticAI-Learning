from google import genai
from google.genai import types

from app.services.llm_service import LLMService
from app.config.llm_config import GOOGLE_CONFIG
from app.tools.registry import ToolRegistry


class GeminiService(LLMService):

    def __init__(self):
        self.config = GOOGLE_CONFIG

        if not self.config.enabled:
            raise ValueError("Gemini provider is disabled.")

        if not self.config.api_key:
            raise ValueError("Gemini API key is not configured.")

        self.client = genai.Client(
            api_key=self.config.api_key
        )

        self.tool_registry = ToolRegistry()

    def decide(self, message: str) -> dict:

        calculate_tool = types.FunctionDeclaration(
            name="calculate",
            description="Perform a mathematical calculation.",
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "a": types.Schema(
                        type="NUMBER",
                        description="First number."
                    ),
                    "operator": types.Schema(
                        type="STRING",
                        description="Mathematical operator: +, -, *, or /."
                    ),
                    "b": types.Schema(
                        type="NUMBER",
                        description="Second number."
                    ),
                },
                required=["a", "operator", "b"],
            ),
        )

        gemini_tool = types.Tool(
            function_declarations=[calculate_tool]
        )

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=message,
            config=types.GenerateContentConfig(
                tools=[gemini_tool],
                automatic_function_calling=types.AutomaticFunctionCallingConfig(
                    disable=True
                ),
            ),
        )

        if response.function_calls:

            function_call = response.function_calls[0]

            return {
                "type": "tool_call",
                "tool": function_call.name,
                "arguments": dict(function_call.args),
            }

        return {
            "type": "final_response",
            "content": response.text,
        }