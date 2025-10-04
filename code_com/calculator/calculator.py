from ..basic_calculator import BasicCalculator

class Calculator(BasicCalculator):
    def square(self, a):
        return a * a

    def power(self, a, b):
        for _ in range(b - 1):
            a *= a
        return a
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot compute square root of negative number")
        return a ** 0.5
    
    def percentage(self, part, whole):
        if whole == 0:
            raise ValueError("Whole cannot be zero for percentage calculation")
        return (part / whole) * 100
    
    def evaluate_expression(self, expression):
        try:
            allowed_chars = "0123456789+-*/(). "
            num1, num2, operation = 0, 0, ""
            if any(char not in allowed_chars for char in expression):
                raise ValueError("Invalid characters in expression")
            for i in expression:
                if i in '1234567890':
                    num1= int(i)
                elif i in '+-*/^':
                    operation = i
            if operation == '+':
                return self.add(num1, num2)
            elif operation == '-':
                return self.subtract(num1, num2)
            elif operation == '*':
                return self.multiply(num1, num2)
            elif operation == '/':
                return self.divide(num1, num2)
            elif operation == '^':
                return self.power(num1, num2)
            else:
                return "Invalid operation"
        except Exception as e:
            return f"Error evaluating expression: {e}"


if __name__ == "__main__":
    calc = Calculator()
    print(calc.square(4))
    print(calc.power(2, 3))
    print(calc.square_root(16))
    print(calc.percentage(25, 100))