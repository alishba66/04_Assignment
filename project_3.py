#Guess the Number Game (user)

import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    guess_the_number()
