from app.tools.calculator import calculate


class AIService:

    def chat(self, message: str):

        if message.startswith("calculate"):

            try:
                parts = message.split()

                if len(parts) != 4:
                    return "Please use this format: calculate 10 + 20"

                a = float(parts[1])
                operator = parts[2]
                b = float(parts[3])

                result = calculate(a, operator, b)

                return f"The answer is {result}"

            except ValueError as error:
                return f"Calculation error: {error}"

        return f"AI says: You entered '{message}'"