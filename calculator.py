import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square_root(x):
    return math.sqrt(x)

def exponential(x, y):
    return x ** y

while True:
    # Get user input for operation and operands
    operation = input("Enter an operation (+, -, *, /, sqrt, exp): ")
    if operation == "sqrt":
        operand1 = float(input("Enter a number: "))
        print("Result: ", square_root(operand1))
    elif operation == "exp":
        operand1 = float(input("Enter base number: "))
        operand2 = float(input("Enter exponent: "))
        print("Result: ", exponential(operand1, operand2))
    else:
        operand1 = float(input("Enter the first number: "))
        operand2 = float(input("Enter the second number: "))
        if operation == "+":
            print("Result: ", add(operand1, operand2))
        elif operation == "-":
            print("Result: ", subtract(operand1, operand2))
        elif operation == "*":
            print("Result: ", multiply(operand1, operand2))
        elif operation == "/":
            print("Result: ", divide(operand1, operand2))
        else:
            print("Invalid operation.")
    cont = input("Do you want to continue? (y/n)")
    if cont == 'n':
        break