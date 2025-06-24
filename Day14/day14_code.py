# Challenge - Calculate factorial recursively

def factorial(n):
    # base case
    if n == 0 or n ==1:
        return 1
    # recursive case
    else:
        return n *factorial(n-1) 
    
# Test the function
try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
