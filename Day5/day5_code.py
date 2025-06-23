# Challenge - Write a function that computes the sum and average of a list of numbers

# way 1 - Basic way using built-in functions
def calculate_sum_avg(numbers):
    total = sum(numbers)
    average = total/len(numbers)
    return total, average

list_of_numbers = [10, 20, 30, 40, 50]
total, average = calculate_sum_avg(list_of_numbers)
print(f"Total: {total}, Average: {average}")

# way 2 - Rebuilt sum() using a lambda inside a loop
def sum_and_average(numbers):
    # Lambda to add two numbers
    add = lambda x, y: x + y

    # Calculate total using a loop and lambda
    total = 0
    for num in numbers:
        total = add(total, num)

    # Calculate average manually
    average = total / len(numbers) if numbers else 0

    return total, average

list_of_numbers = [200, 120, 350, 403, 500]
total, average = sum_and_average(list_of_numbers)
print(f"Total: {total}, Average: {average}")

