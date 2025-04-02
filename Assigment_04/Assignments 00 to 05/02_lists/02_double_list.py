# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# Define the function to double each element in the list
def double_list(numbers):
    # Use a list comprehension to double each element
    return [number * 2 for number in numbers]

# Test the function with the given list
numbers = [1, 2, 3, 4]
doubled_numbers = double_list(numbers)
print(doubled_numbers)  # Output: [2, 4, 6, 8]
