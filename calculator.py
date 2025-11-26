# calculator.py
def main():
    print("Simple Calculator")
    print("Select operation: +, -, *, /")
    op = input("Operation: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
