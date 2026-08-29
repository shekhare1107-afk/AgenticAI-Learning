from app.tools.calculator import calculate
from app.tools.temperature import convert_temperature
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
            ),

            "convert_temperature": ToolDefinition(
                name="convert_temperature",
                description="Convert a temperature between Celsius and Fahrenheit",
                parameters={
                    "value": {
                        "type": "number",
                        "description": "Temperature value to convert",
                    },
                    "from_unit": {
                        "type": "string",
                        "description": "Current unit: celsius or fahrenheit",
                    },
                    "to_unit": {
                        "type": "string",
                        "description": "Target unit: celsius or fahrenheit",
                    },
                },
                function=convert_temperature,
            )
        }

    def get_tool(self, name: str):
        return self.tools.get(name)

    def get_schemas(self) -> list[dict]:
        return [
            tool.to_schema()
            for tool in self.tools.values()
        ]