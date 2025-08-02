# Ask for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result} - calc.py:11")
elif operation == "-":
    result = num1 - num2
    print(f"{num1}  {num2} = {result} - calc.py:14")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result} - calc.py:17")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result} - calc.py:21")
    else:
        print("Error: Division by zero is not allowed. - calc.py:23")
else:
    print("Invalid operation. Please use +, , *, or /. - calc.py:25")

