# Hangman

import random

def choose_word():
    words = ['python', 'hangman', 'developer', 'challenge', 'keyboard']
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

def hangman():
    print("🎮 Welcome to Hangman!\n")
    secret_word = choose_word()
    guessed_letters = set()
    tries = 6  # Number of allowed wrong guesses

    while tries > 0:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Correct guess!")
        else:
            print("❌ Wrong guess!")
            tries -= 1

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n🎉 You guessed the word: {secret_word}")
            break
    else:
        print(f"\n💀 Game over! The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
