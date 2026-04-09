# ================================
# SIMPLE CALCULATOR (BEGINNER)
# ================================

print("=== SIMPLE CALCULATOR ===")

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid operator")


# ================================
# FUNCTION-BASED CALCULATOR
# ================================

print("\n=== FUNCTION CALCULATOR ===")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


n1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
n2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", add(n1, n2))

elif operator == "-":
    print("Result:", subtract(n1, n2))

elif operator == "*":
    print("Result:", multiply(n1, n2))

elif operator == "/":
    print("Result:", divide(n1, n2))

else:
    print("Invalid operator")
