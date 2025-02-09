# My Calculator

def calculate(x, y, operation):
    if operation == "+":
        return x + y
    if operation == "-":
        return x - y
    if operation == "*":
        return x * y
    if operation == "/":
        return x / y

running = True

while running:
    print("Type '+' for Add")
    print("Type '-' for Subtract")
    print("Type '*' for Multiply")
    print("Type '/' for Divide")
    operation = input("Select an operation: ")
    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation")
        running = False
        break
    numbers_input = input("Select the both first and second number separated by ' ': ")
    numbers_arr = numbers_input.split(" ")
    if len(numbers_arr) > 2:
        print("Too many numbers")
        running = False
        break
    result = calculate(float(numbers_arr[0]), float(numbers_arr[1]), operation)
    print(float(numbers_arr[0]), " ", operation, " ", float(numbers_arr[1]), " = ", result)
