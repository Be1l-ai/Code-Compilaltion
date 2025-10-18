import sys
import os

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from code_com.basic_calculator import BasicCalculator

class Calculator(BasicCalculator):
    def square(self, a):
        return a * a

    def power(self, a, b):
        result = 1
        for _ in range(int(b)):
            result *= a
        return result
    
    def square_root(self, a):
        if a < 0:
            return "Error: can't do square root of negative number"
        return a ** 0.5
    
    def percentage(self, part, whole):
        if whole == 0:
            return "Error: can't divide by zero"
        return (part / whole) * 100
    
    def evaluate_expression(self, expression):
        try:
            expression = expression.replace(" ", "")
            result = eval(expression)  # yeah i know eval is not safe but works for now
            return result
        except ZeroDivisionError:
            return "Error: Division by zero!"
        except SyntaxError:
            return "Error: Invalid expression syntax"
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    calc = Calculator()
    print("Testing square:")
    print(f"  4² = {calc.square(4)}")
    print("\nTesting power:")
    print(f"  2³ = {calc.power(2, 3)}")
    print("\nTesting evaluate_expression:")
    print(f"  2 + 3 = {calc.evaluate_expression('2 + 3')}")
    print(f"  10 * 5 = {calc.evaluate_expression('10 * 5')}")
    print(f"  100 / 4 = {calc.evaluate_expression('100 / 4')}")