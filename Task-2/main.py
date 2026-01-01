print("Simple Calculator")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operation = input(
        "Choose operation (+, -, *, /): "
    ).strip()

    if operation == "+":
        result = num1 + num2
        print("Result:", result)

    elif operation == "-":
        result = num1 - num2
        print("Result:", result)

    elif operation == "*":
        result = num1 * num2
        print("Result:", result)

    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero not allowed.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid operation selected.")

except ValueError:
    print("Please enter valid numeric values.")
