# Project 2: Guess the Number Game Python Project (computer)

import random

def generate_random_number():
    """
    Generates a random number between 1 and 100.
    """
    return random.randint(1, 100)

def play_game():
    """
    Main function for the Guess the Number Game.
    """
    random_number = generate_random_number()
    attempts = 0
    max_attempts = 5
    
    
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("Good luck!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
        if attempts == max_attempts:
            print(f"Sorry, you've used all your attempts. The number was {random_number}.")
            break
        
play_game()