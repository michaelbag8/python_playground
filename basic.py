import numpy as np


def calculate(first_number, operator, second_number):
    """Perform a basic calculation with NumPy."""
    operations = {
        "+": np.add,
        "-": np.subtract,
        "*": np.multiply,
        "/": np.divide,
    }

    if operator not in operations:
        raise ValueError("Operator must be one of: +, -, *, /")
    if operator == "/" and second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return operations[operator](first_number, second_number)


def main():
    print("Basic NumPy Calculator")
    print("Enter q at any prompt to quit.")

    while True:
        first_value = input("First number: ")
        if first_value.lower() == "q":
            break

        operator = input("Operator (+, -, *, /): ")
        if operator.lower() == "q":
            break

        second_value = input("Second number: ")
        if second_value.lower() == "q":
            break

        try:
            result = calculate(float(first_value), operator, float(second_value))
            print(f"Result: {result:g}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()