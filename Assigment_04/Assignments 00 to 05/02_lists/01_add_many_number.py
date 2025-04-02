# Write a function that takes a list of numbers and returns the sum of those numbers.


#function to take a list of numbers
def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#testing the function
numbers = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers)
print("The sum of the numbers is:", result)

