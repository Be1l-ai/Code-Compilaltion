# Math Utilities Documentation

## Overview
The **Math Utilities** module provides basic mathematical functions commonly used in computations. This module includes functions for calculating factorials, checking prime numbers, and finding the greatest common divisor (GCD).

## Functions

### 1. `factorial(n)`
**Description:**
Calculates the factorial of a given non-negative integer `n`.

**Parameters:**
- `n` (int): The number to compute the factorial for.

**Returns:**
- `int`: The factorial of `n` if `n >= 0`.
- `str`: Error message if `n < 0`.

**Example Usage:**
```python
print(factorial(5))  # Output: 120
```

---

### 2. `is_prime(n)`
**Description:**
Checks whether a given number `n` is prime.

**Parameters:**
- `n` (int): The number to check.

**Returns:**
- `bool`: `True` if `n` is a prime number, `False` otherwise.

**Example Usage:**
```python
print(is_prime(7))  # Output: True
print(is_prime(10)) # Output: False
```

---

### 3. `gcd(a, b)`
**Description:**
Finds the greatest common divisor (GCD) of two integers `a` and `b`.

**Parameters:**
- `a` (int): First number.
- `b` (int): Second number.

**Returns:**
- `int`: The greatest common divisor of `a` and `b`.

**Example Usage:**
```python
print(gcd(48, 18))  # Output: 6
```

## Usage
This module can be imported into other Python scripts or executed as a standalone script to test the functions.

```python
from math_utils import factorial, is_prime, gcd

print(factorial(5))
print(is_prime(11))
print(gcd(81, 27))
```

## Author
This module was created as part of my coding documentation and compilation project.
