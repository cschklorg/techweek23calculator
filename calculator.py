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
        
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = None
    while choice not in ['1', '2', '3', '4']:
        choice = input("Enter choice (1, 2, 3, 4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = add(num1, num2)
        operation = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "*"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "/"
    else:
        print("Invalid input")
        exit()
    
    print(f"\n{num1} {operation} {num2} = {result}\n")