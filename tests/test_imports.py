#This file shows various ways to import from the code package.

import sys
import os

# Add the parent directory to sys.path to import the 'code' package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Method 1: Import the entire package
import code_com as code

# Method 2: Import specific modules
from code_com import BasicCalculator, Chatbot, MathUtils

# Method 3: Import from submodules directly
from code_com.minigames import jack_en_poy, guess_number, math_prob

# Method 4: Import submodule packages
from code_com import basic_calculator, chatbot, math_utils, minigames


def test_basic_calculator():
    """Test the BasicCalculator class."""
    calc = BasicCalculator()
    print("Testing BasicCalculator:")
    print(f"  5 + 3 = {calc.add(5, 3)}")
    print(f"  10 - 4 = {calc.subtract(10, 4)}")
    print(f"  6 * 7 = {calc.multiply(6, 7)}")
    print(f"  15 / 3 = {calc.divide(15, 3)}")
    print(f"  10 / 0 = {calc.divide(10, 0)}")
    print()


def test_math_utils():
    """Test the MathUtils class."""
    print("Testing MathUtils:")
    print(f"  Factorial of 5: {MathUtils.factorial(5)}")
    print(f"  Is 7 prime? {MathUtils.is_prime(7)}")
    print(f"  Is 10 prime? {MathUtils.is_prime(10)}")
    print(f"  GCD of 48 and 18: {MathUtils.gcd(48, 18)}")
    print()


def test_chatbot():
    """Test the Chatbot class (without interactive mode)."""
    print("Testing Chatbot:")
    bot = Chatbot()
    print(f"  Bot responses available: {len(bot.responses)}")
    print(f"  Sample response keys: {list(bot.responses.keys())[:3]}")
    print()


def test_imports():
    """Test that all imports work correctly."""
    print("Testing imports:")
    print(f"  code package version: {code.__version__}")
    print(f"  Available in code package: {code.__all__}")
    print()
    
    # Test that classes can be instantiated
    calc = code.BasicCalculator()
    bot = code.Chatbot()
    print("  ✓ All imports successful!")
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("Running tests for the code package")
    print("=" * 60)
    print()
    
    test_imports()
    test_basic_calculator()
    test_math_utils()
    test_chatbot()
    
    print("=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)
    print()
    print("Note: Minigame functions (jack_en_poy, guess_number, math_prob)")
    print("are interactive and should be called separately.")
