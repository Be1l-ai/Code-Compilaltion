class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

if __name__ == "__main__":
    calc = BasicCalculator()
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", calc.add(num1, num2))
    elif operator == "-":
        print("Result:", calc.subtract(num1, num2))
    elif operator == "*":
        print("Result:", calc.multiply(num1, num2))
    elif operator == "/":
        print("Result:", calc.divide(num1, num2))
    else:
        print("Invalid operator!")
