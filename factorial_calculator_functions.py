# factorial_calculator_functions.py

"""
This module contains a function to calculate the factorial of a number.
The factorial is calculated using recursion. The program asks the user for 
input and displays the factorial of the given number.
"""

def factorial(n: int) -> int:
    """
    Calculates the factorial of a number using recursion.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.
    """
    if n in (0, 1):  # Refactored to use 'in' instead of 'or'
        return 1
    return n * factorial(n - 1)

def main():
    """
    Main function to ask for user input and print the factorial of the entered number.
    """
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
    except ValueError:
        print("Please enter a valid integer.")

# If the script is being run directly, call the main function
if __name__ == "__main__":
    main()
