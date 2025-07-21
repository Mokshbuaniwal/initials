# here i will make a calculator

#+ - * \ \\ % ** 

# here calc start
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operation (add , sub , multi , div , div with nearest integer , exponation , reminder ): ")

if c == "add":
    print(f"Result: {a + b}")
elif c == "sub":
    print(f"Result: {a - b}")
elif c == "multi":
    print(f"Result: {a * b}")
elif c == "div":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Division by zero is not allowed.")
elif c == "div with nearest integer":
    if b != 0:
        print(f"Result: {a // b}")
    else:
        print("Error: Division by zero is not allowed.")
elif c == "exponation":
    print(f"Result: {a ** b}")
elif c == "reminder":
    if b != 0:
        print(f"Result: {a % b}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please choose from add, sub, multi, div, div with nearest integer, exponation, or reminder.")

