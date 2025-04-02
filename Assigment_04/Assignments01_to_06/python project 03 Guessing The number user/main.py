import random

def play_game():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    low, high = 1, 100
    attempts = 0
    feedback = ' '

    while feedback != 'C':
        if low > high:
            print("It seems like you're not playing fair!")
            break
        guess = random.randint(low, high)
        feedback = input(f"My guess is {guess}..! \nIs my guess too high (H), too low (L), or correct (C)? ").strip().upper()
        attempts += 1
        if feedback == 'H':
            high = guess - 1
            print ('Check your guess again!')
        elif feedback == 'L':
            low = guess + 1
            print ('Check your guess again!')
        elif feedback == 'C':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
        else:
            print("Please respond with H, L, or C.")
            
        if attempts == 5:
            print("Sorry! You have used all your attempts.") 
            break
    print("Thanks for playing!")
    
play_game()