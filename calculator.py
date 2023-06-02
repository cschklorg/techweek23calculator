import math
while True:
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        return x / y
        
    def power(x, y):
        return x ** y
    
    def root(x):
        return math.sqrt(x)
    
    def sine(x):
        return math.sin(math.radians(x))

    def cosine(x):
        return math.cos(x)
    
    def tangent(x):
        return math.tan(math.radians(x))
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")

    choice = None
    while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        choice = input("Enter choice (1, 2, 3, 4, 5, 6, 7, 8, 9): ")
    
    if choice == '1':
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        operation = "+"
        print(f"\n{num1} {operation} {num2} = {result}\n")

    elif choice == '2':
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        result = subtract(num1, num2)
        operation = "-"
        print(f"\n{num1} {operation} {num2} = {result}\n")

    elif choice == '3':
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiply(num1, num2)
        operation = "*"
        print(f"\n{num1} {operation} {num2} = {result}\n")

    elif choice == '4':
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        result = divide(num1, num2)
        operation = "/"
        print(f"\n{num1} {operation} {num2} = {result}\n")

    elif choice == '5':
        num1 = float(input("\nEnter base number: "))
        num2 = float(input("Enter index number: "))
        result = power(num1, num2)
        operation = "**"
        print(f"\n{num1} {operation} {num2} = {result}\n")

    elif choice == '6':
        num1 = float(input("\nEnter the number: "))
        result = root(num1)
        print(result, "\n")

    elif choice == '7':
        num1 = float(input("\nEnter the degree: "))
        result = sine(num1)
        print(result, "\n")

    elif choice == '8':
        num1 = float(input("\nEnter the radian: "))
        result = cosine(num1)
        print(result, "\n")

    elif choice == '9':
        num1 = float(input("\nEnter the degree: "))
        result = tangent(num1)
        print(result, "\n")

    else:
        print("Invalid input")
        exit()