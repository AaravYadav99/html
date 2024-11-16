def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
number = 5
print("Factorial (Recursive) of", number, "is", factorial_recursive(number))
