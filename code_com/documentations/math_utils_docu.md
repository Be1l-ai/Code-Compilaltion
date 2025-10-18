# Math Utilities

Collection of mathematical utility functions.

## Features

Static methods for common math operations:

- `factorial(n)` — Calculate factorial
- `is_prime(n)` — Check if number is prime
- `gcd(a, b)` — Greatest common divisor
- `lcm(a, b)` — Least common multiple

## Why Static Methods?

used @staticmethod decorator because:
- don't need to create instances (like `utils = MathUtils()`)
- these functions are self-contained
- just utility functions, no state to maintain
- cleaner to use: `MathUtils.factorial(5)` vs `utils.factorial(5)`

## Performance Notes

- **factorial:** uses iteration (safer than recursion for large numbers)
- **is_prime:** only checks up to sqrt(n) for efficiency
- **gcd:** euclidean algorithm is super fast
- **lcm:** depends on gcd so it's also efficient

## What I Learned

- static methods and when to use them
- prime number algorithms
- mathematical concepts in code
- importance of handling edge cases

## Limitations

- factorial can get huge fast (might overflow for very large numbers)
- no input validation for types (assumes you pass integers)
- prime checker is basic (for serious use there are better algorithms)
- no floating point support (integers only)
