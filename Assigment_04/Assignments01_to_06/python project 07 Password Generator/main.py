# Project 7: Password Generator Python Project BY Hammad Ahmed..!

import random
import string

def generate_password():
    # Define the length of the password
    length = int(input("Enter the length of the password: "))

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Call the function to generate the password
password = generate_password()
print("Generated Password: ", password)

