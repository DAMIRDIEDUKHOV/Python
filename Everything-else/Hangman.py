import random

def hangman():
    # List of words to choose from
    word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "mango"]

    # Select a random word from the list
    secret_word = random.choice(word_list)

    # Initialize the display word with underscores
    display_word = "_" * len(secret_word)

    # Track the guessed letters and remaining attempts
    guessed_letters = []
    attempts = 7

    # Hangman ASCII art images
    hangman_images = [
        '''
           ____
          |    |
          |    
          |   
          |    
          |   
        _|_
        ''',
        '''
           ____
          |    |
          |    O
          |   
          |    
          |   
        _|_
        ''',
        '''
           ____
          |    |
          |    O
          |    |
          |    |
          |   
        _|_
        ''',
        '''
           ____
          |    |
          |    O
          |   /|
          |    |
          |   
        _|_
        ''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |    |
          |   
        _|_
        ''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |    |
          |   /
        _|_
        ''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |    |
          |   / \\
        _|_
        '''
    ]

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        print("\nAttempts remaining:", attempts)
        print(hangman_images[7 - attempts])
        print("Word:", display_word)
        print("Guessed letters:", ", ".join(guessed_letters))

        # Get player's guess
        guess = input("Guess a letter: ").lower()

        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            # Update the display word with the correctly guessed letter
            display_word = "".join(
                letter if letter == guess else display_word[i] for i, letter in enumerate(secret_word)
            )
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1

        # Check if the player has won or lost
        if display_word == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break
        elif attempts == 0:
            print("Sorry, you lost. The word was:", secret_word)
            break

hangman()