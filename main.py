# main.py

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def is_even(number):
    """Return True if the number is even, else False."""
    return number % 2 == 0

if __name__ == "__main__":
    # Example usage
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"Is 4 even? {is_even(4)}")
