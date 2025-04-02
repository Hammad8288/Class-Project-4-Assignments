# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

def main():
    # Prompt the user to enter the first number
    first_number = int(input("Enter the first number: "))

    # Prompt the user to enter the second number
    second_number = int(input("Enter the second number: "))
    
    # Calculate the sum of the two numbersr6
    total_sum = first_number + second_number
    
    print ("The Sum of First Number & Second Number is", total_sum )
    
if __name__ == "__main__":
    main()