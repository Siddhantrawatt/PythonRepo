def sum(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

sum = sum(5, 3)
subtract = subtract(5, 3)
multiply = multiply(5, 3)
divide = divide(5, 3)
print("Sum:", sum)
print("Subtract:", subtract)
print("Multiply:", multiply)
print("Divide:", divide)
