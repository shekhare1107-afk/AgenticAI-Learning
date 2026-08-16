from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class ToolDefinition:
    name: str
    description: str
    parameters: dict[str, Any]
    function: Callable[..., Any]

    def to_schema(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": self.parameters,
                "required": list(self.parameters.keys()),
            },
        }