def calculate(a: float, operator: str, b: float) -> float:

    if operator == "+":
        return a + b

    if operator == "-":
        return a - b

    if operator == "*":
        return a * b

    if operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    raise ValueError(f"Unsupported operator: {operator}")