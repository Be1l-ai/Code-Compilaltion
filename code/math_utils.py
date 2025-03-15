def factorial(n):
    if n < 0:
        return "Error! Factorial of a negative number doesn't exist."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        i = 2
        while i <= n:
            result *= i
            i += 1
        return result

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

num = 5
print("Factorial of", num, "is", factorial(num))
prime_test = 7
print("Is", prime_test, "a prime number?", is_prime(prime_test))
a, b = 48, 18
print("GCD of", a, "and", b, "is", gcd(a, b))
