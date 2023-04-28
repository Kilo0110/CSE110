import random

list_of_words = ['programmer', 'developer', 'student', 'pathway', 'python']

secret_word = random.choice(list_of_words)

# Initialize the list of guessed letters with underscores
guessed_letters = ["_" for letter in secret_word]

# Keep track of the number of guesses
number_of_guesses = 0

# Play the game until the word is guessed
while "_" in guessed_letters:
    # Print the current state of the word
    print(" ".join(guessed_letters))

    # Get the user's guess
    guess = input("Enter a guess: ")

    # Increment the number of guesses
    number_of_guesses += 1

    # Check if the guess is the correct length
    if len(guess) != len(secret_word):
        print(f"Your guess must be {len(secret_word)} letters long.")
        continue

    # Check if the guess is correct
    if guess.lower() == secret_word:
        print("Congratulations, you guessed the word!")
        # Print the number of guesses
        if number_of_guesses == 1:
          print(f"It took you {number_of_guesses} guess! Amazing!")
        elif number_of_guesses <= 3:
          print(f"It took you {number_of_guesses} guesses! Not bad!")
        else:
          print(f"It took you {number_of_guesses} guesses! Better luck next time")
        exit()
        break

    # Otherwise, generate a hint for the user
    hint = []
    for i, letter in enumerate(guess): # turn the guess into an enumerable to allow me loop through each letter
        if letter == secret_word[i]: # if the letter is in the right position in the secret word
            hint.append(letter.upper())
        elif letter in secret_word: # if the letter is in secret word but not in the right position
            hint.append(letter.lower())
        else:
            hint.append(" _ ")

    # Print the hint for the user
    print("".join(hint))
