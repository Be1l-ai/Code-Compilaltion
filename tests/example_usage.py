#This file demonstrates various ways to use the code package in different scenarios.
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from code_com import BasicCalculator, Chatbot, MathUtils
from code_com.minigames import jack_en_poy, guess_number, math_prob


def example_basic_calculator():
    """Example: Using the BasicCalculator class."""
    print("=" * 60)
    print("Example 1: Basic Calculator")
    print("=" * 60)
    
    calc = BasicCalculator()
    
    # Perform calculations
    operations = [
        ("10 + 5", calc.add(10, 5)),
        ("10 - 5", calc.subtract(10, 5)),
        ("10 * 5", calc.multiply(10, 5)),
        ("10 / 5", calc.divide(10, 5)),
        ("10 / 0", calc.divide(10, 0)),
    ]
    
    for operation, result in operations:
        print(f"  {operation} = {result}")
    
    print()


def example_math_utils():
    """Example: Using the MathUtils class."""
    print("=" * 60)
    print("Example 2: Math Utils")
    print("=" * 60)
    
    # Factorial examples
    print("Factorials:")
    for n in [0, 1, 5, 10]:
        print(f"  {n}! = {MathUtils.factorial(n)}")
    
    print()
    
    # Prime number examples
    print("Prime number checks:")
    for n in [2, 7, 10, 17, 20, 29]:
        is_prime = MathUtils.is_prime(n)
        print(f"  {n} is {'prime' if is_prime else 'not prime'}")
    
    print()
    
    # GCD examples
    print("GCD calculations:")
    pairs = [(48, 18), (100, 50), (17, 19), (56, 98)]
    for a, b in pairs:
        print(f"  GCD({a}, {b}) = {MathUtils.gcd(a, b)}")
    
    print()


def example_chatbot():
    """Example: Using the Chatbot class (non-interactive)."""
    print("=" * 60)
    print("Example 3: Chatbot")
    print("=" * 60)
    
    bot = Chatbot()
    
    print("Available responses:")
    for key, response in bot.responses.items():
        print(f"  Input: '{key}'")
        print(f"  Response: '{response}'")
        print()
    
    print("Note: Call bot.chat() for interactive mode")
    print()


def example_combined_usage():
    """Example: Combining multiple modules."""
    print("=" * 60)
    print("Example 4: Combined Usage - Simple Math Problem Solver")
    print("=" * 60)
    
    calc = BasicCalculator()
    
    # Use calculator and math utils together
    a, b = 12, 8
    
    print(f"Given numbers: {a} and {b}")
    print()
    
    print("Basic operations:")
    print(f"  Sum: {calc.add(a, b)}")
    print(f"  Difference: {calc.subtract(a, b)}")
    print(f"  Product: {calc.multiply(a, b)}")
    print(f"  Quotient: {calc.divide(a, b)}")
    print()
    
    print("Advanced operations:")
    print(f"  GCD: {MathUtils.gcd(a, b)}")
    print(f"  Factorial of {a}: {MathUtils.factorial(a)}")
    print(f"  Is {a} prime? {MathUtils.is_prime(a)}")
    print(f"  Is {b} prime? {MathUtils.is_prime(b)}")
    print()


def example_minigames_info():
    """Example: Information about minigames."""
    print("=" * 60)
    print("Example 5: Minigames Information")
    print("=" * 60)
    
    games = [
        ("jack_en_poy", jack_en_poy, "Rock-Paper-Scissors game"),
        ("guess_number", guess_number, "Guess a number between 1-100"),
        ("math_prob", math_prob, "Math quiz game with score tracking"),
    ]
    
    print("Available games:")
    for name, func, description in games:
        print(f"  • {name}(): {description}")
    
    print()
    print("To play a game, call the function:")
    print("  Example: jack_en_poy()")
    print()
    print("Note: These are interactive games - not running them in this demo")
    print()


def main():
    """Run all examples."""
    print("\n")
    print("#" * 60)
    print("#" + " " * 58 + "#")
    print("#" + "  CODE PACKAGE - USAGE EXAMPLES".center(58) + "#")
    print("#" + " " * 58 + "#")
    print("#" * 60)
    print("\n")
    
    example_basic_calculator()
    example_math_utils()
    example_chatbot()
    example_combined_usage()
    example_minigames_info()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
