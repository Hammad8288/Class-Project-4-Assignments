import random

# Hangman Stages (Visual Representation)
hangman_pics = [
    """ 
       ------
       |    |
       |    
       |   
       |    
       |
    --------
    """,
    """ 
       ------
       |    |
       |    O
       |   
       |    
       |
    --------
    """,
    """ 
       ------
       |    |
       |    O
       |    |
       |    
       |
    --------
    """,
    """ 
       ------
       |    |
       |    O
       |   /|
       |    
       |
    --------
    """,
    """ 
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    --------
    """,
    """ 
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """ 
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Word list
words = ["python", "streamlit", "developer", "code", "computer"]

# Select a random word
word = random.choice(words)
word_display = ["_"] * len(word)  # Display with underscores
attempts = 0
max_attempts = len(hangman_pics) - 1  # Max attempts before game over
guessed_letters = []

print("🎮 Welcome to Hangman Game 🎮")
print(hangman_pics[0])  # Initial empty hangman

while attempts < max_attempts:
    print("\nWord: " + " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = guess
        print("✅ Good guess!")
    else:
        attempts += 1
        print("❌ Wrong guess! Try again.")
        print(hangman_pics[attempts])

    if "_" not in word_display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

if "_" in word_display:
    print("\n💀 Game Over! The word was:", word)
