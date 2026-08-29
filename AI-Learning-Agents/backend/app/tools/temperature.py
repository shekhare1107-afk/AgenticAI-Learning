def convert_temperature(
    value: float,
    from_unit: str,
    to_unit: str,
) -> float:

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9 / 5) + 32

    if from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5 / 9

    if from_unit == to_unit:
        return value

    raise ValueError(
        f"Unsupported temperature conversion: {from_unit} to {to_unit}"
    )