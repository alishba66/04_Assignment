# Guess the Number Game Python Project computer

def computer_guesses_number():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    print("Respond with: 'too low', 'too high', or 'correct'\n")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"My guess is: {guess}")
        feedback = input("Your response (too low / too high / correct): ").strip().lower()

        if feedback == 'too low':
            low = guess + 1
        elif feedback == 'too high':
            high = guess - 1
        elif feedback == 'correct':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        else:
            print("Invalid input. Please respond with 'too low', 'too high', or 'correct'.\n")

if __name__ == '__main__':
    computer_guesses_number()
