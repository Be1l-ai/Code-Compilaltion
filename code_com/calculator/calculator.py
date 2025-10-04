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
            if any(char not in allowed_chars for char in expression):
                raise ValueError("Invalid characters in expression")
            
            expression = expression.replace(" ", "")
            
            num1 = ""
            operation = ""
            num2 = ""
            
            i = 0
            while i < len(expression):
                char = expression[i]
                if char.isdigit() or char == '.':
                    num1 += char
                elif char in '+-*/^':
                    operation = char
                    num2 = expression[i+1:]
                    break
                else:
                    raise ValueError("Unexpected character")
                i += 1
            
            if not num1 or not operation or not num2:
                return "Invalid expression: Missing parts"
            
            num2 = ''.join(c for c in num2 if c.isdigit())
            if not num2:
                return "Invalid second number"
            
            n1, n2 = float(num1), float(num2)
            
            if operation == '+':
                return self.add(n1, n2)
            elif operation == '-':
                return self.subtract(n1, n2)
            elif operation == '*':
                return self.multiply(n1, n2)
            elif operation == '/':
                return self.divide(n1, n2)
            elif operation == '^':
                return self.power(n1, n2)
            else:
                return "Invalid operation"
        
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Error evaluating: {e}"


if __name__ == "__main__":
    calc = Calculator()
    print(calc.square(4))
    print(calc.evaluate_expression("2 + 3"))