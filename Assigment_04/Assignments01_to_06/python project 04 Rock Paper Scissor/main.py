# Project 4: Rock, paper, scissors Python Project By Hammad Ahmed..!
# Game jeetne ke rules apply honge:

# Rock beats Scissors 🪨✂️

# Scissors beats Paper ✂️📄

# Paper beats Rock 📄🪨

import random

def play_game():
    print("Welcome to Rock, Paper, Scissors Game..!")
    print("You have 3 chances to win the game.")
    print("Let's start the game!")
    
    
    # Initialize chances and user choice
while True:
    chances = 0
    user_choice = ""
    choices = ["rock", "paper", "scissors"]
    
    #for quiting the game
    if user_choice == "quit":
            print("Thanks for playing! 🎉")
            break  # Exit game
        
    #for invalid input
    user_choice = input(f"Enter your choice {choices}: ").lower().strip()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    # comparing choices
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")
        
    chances += 1
    if chances >= 3:
        print("Game over! You've used all your chances.")
        break

play_game()