# here i will make a calculator

#+ - * \ \\ % ** 

# here calc start
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operation (add , sub , multi , div , div with nearest integer , exponation , reminder ,  percentage , factorial): ")



if c == "add" or c == "+":
    print(f"Result: {a + b}")
elif c == "sub" or c == "-":

    print(f"Result: {a - b}")
elif c == "multi" or c == "*":
    print(f"Result: {a * b}")
elif c == "div" or c == "/":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Division by zero is not allowed.")
elif c == "div with nearest integer":
    if b != 0 :
        print(f"Result: {a // b}")
    else:
        print("Error: Division by zero is not allowed.")
elif c == "exponation":
    print(f"Result: {a ** b}")
elif c == "reminder" or c == "%":
    if b != 0:
        print(f"Result: {a % b}")
    else:
        print("Error: Division by zero is not allowed.")
elif c == "percentage":
    if b != 0:
        print(f"Result: {(a / b) * 100}%")
    else:
        print("Error: Division by zero is not allowed.")
elif c == "factorial":
    import math
    if a >= 0:
        print(f"Result: {math.factorial(a)}")
    else:
        print("Error: Factorial is not defined for negative numbers.")
else:
    print("Invalid operation! Please choose from add, sub, multi, div, div with nearest integer, exponation, or reminder.")