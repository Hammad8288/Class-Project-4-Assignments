# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.

import random

Num_Rounds = 5

def get_valid_guess():
    while True:
        guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()
        if guess in ['higher', 'lower']:
            return guess
        else:
            print("Invalid input. Please enter 'higher' or 'lower'.")

def game():
    Score = 0
    
    print("Welcome to the High-Low game!")
    print("You will play", Num_Rounds, "rounds.")
    
    # Loop through the number of rounds
    for Round in range(Num_Rounds):
        
        # Generate a random number for the user and the computer
        user = random.randint(1, 100)
        computer = random.randint(1, 100)
        print("\nRound", Round + 1)

        # Get the user's guess
        print("Your number is:", user)
        print("The computer's number is hidden.")
        
        #determin actural results
        guess = get_valid_guess()
        if user > computer:
            actual_result = "higher"
        elif user < computer:
            actual_result = "lower"
        else:
            actual_result = "equal"
            
        # Check if the user's guess matches the actual result
        if guess == actual_result:
            print(f"You were right! The computer's number was {computer}")
            Score += 1
        elif actual_result == "equal":
            print(f"Aww, that's incorrect. The computer's number was also {computer}. You lose this round!")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer}. You lose this round!")
            
         # Print current score
    print(f"Your score is now {Score}")

     # Final message based on score
    print("\nThanks for playing!")

    if Score == Num_Rounds:
        print("Congratulations! You won the game!")
    elif Score >= Num_Rounds / 2:
        print("Good job! You did well!")
        print("You might want to try again next time.")
    else:
        print("Better luck next time!")
            
game()