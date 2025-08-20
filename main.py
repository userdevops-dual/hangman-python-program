import random
import time

# Hangman drawings (6 stages, 0 = full hangman)
HANGMAN = [
    """
     -----
     |   |
     |   O
     |  /|\\
     |  / \\
     |
    _|_
    """,
    """
     -----
     |   |
     |   O
     |  /|\\
     |  / 
     |
    _|_
    """,
    """
     -----
     |   |
     |   O
     |  /|\\
     |  
     |
    _|_
    """,
    """
     -----
     |   |
     |   O
     |  /|
     |  
     |
    _|_
    """,
    """
     -----
     |   |
     |   O
     |   |
     |  
     |
    _|_
    """,
    """
     -----
     |   |
     |   O
     |
     |
     |
    _|_
    """,
    """
     -----
     |   |
     |
     |
     |
     |
    _|_
    """,
]

# Words file se read karo
with open('words.txt', 'r') as file:
    words = file.read().splitlines()

# Random word choose karo
random_word = random.choice(words).lower()

# Hidden word banado underscores me
hidden = ["_"] * len(random_word)

# Starting message
print("Starting the game...")
time.sleep(1)
print(" ".join(hidden))

# Total lives (hangman ke steps jitne ho sakte hain)
lives = len(HANGMAN) - 1

# Game loop
while True:
    guess = input("Enter a letter: ").lower()

    # Track correct guess
    correct_guess = False

    # Check har letter me
    for index, letter in enumerate(random_word):
        if letter == guess:
            hidden[index] = guess
            correct_guess = True

    # Agar guess correct tha
    if correct_guess:
        print(f"✅ You guessed the letter '{guess}' correctly!")
    else:
        lives -= 1
        print(f"❌ Wrong guess! Lives remaining: {lives}")
        print(HANGMAN[len(HANGMAN) - 1 - lives])  # show hangman stage

    # Current state print karo
    print(" ".join(hidden))

    # Win condition
    if "_" not in hidden:
        print(f"🎉 Congratulations! You guessed the word: {random_word}")
        break

    # Lose condition
    if lives == 0:
        print(HANGMAN[0])  # full hangman
        print(f"💀 Game Over! The word was: {random_word}")
        break
