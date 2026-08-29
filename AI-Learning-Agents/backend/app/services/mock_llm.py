from app.services.llm_service import LLMService


class MockLLM(LLMService):

    def decide(self, message: str) -> dict:

        parts = message.split()

        if len(parts) == 4 and parts[0].lower() == "calculate":

            try:
                a = float(parts[1])
                operator = parts[2]
                b = float(parts[3])

                return {
                    "type": "tool_call",
                    "tool": "calculate",
                    "arguments": {
                        "a": a,
                        "operator": operator,
                        "b": b,
                    },
                }

            except ValueError:
                return {
                    "type": "final_response",
                    "content": "I could not understand the numbers in your calculation.",
                }

        return {
            "type": "final_response",
            "content": f"I received: {message}",
        }