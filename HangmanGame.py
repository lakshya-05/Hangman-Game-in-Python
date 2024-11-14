# Hangman Game
import random


def hangman():
    words = ["python", "algorithms", "object", "class", "statement", "laptop", "mobile", "friends", "family", "bug"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman")

    while attempts > 0:
        print("\n" + " ".join(guessed_word))
        guess = input("Guess a letter : ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
            guessed_letters.add(guess)
        else:
            print(f"Letter {guess} is not in the word.")
            attempts -= 1
            guessed_letters.add(guess)

        if "_" not in guessed_word:
            print("\nCongratulations, you guessed the word:", word)
            break
        print(f"Remaining attempts: {attempts}")

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", word)


# Main fxn
hangman()
