from app.tools.calculator import calculate
from app.tools.tool_definition import ToolDefinition


class ToolRegistry:

    def __init__(self):
        self.tools = {
            "calculate": ToolDefinition(
                name="calculate",
                description="Perform a mathematical calculation",
                parameters={
                    "a": {
                        "type": "number",
                        "description": "First number",
                    },
                    "operator": {
                        "type": "string",
                        "description": "Mathematical operator: +, -, *, or /",
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number",
                    },
                },
                function=calculate,
            )
        }

    def get_tool(self, name: str):
        return self.tools.get(name)

    def get_schemas(self) -> list[dict]:
        return [
            tool.to_schema()
            for tool in self.tools.values()
        ]