# Rock, paper, scissors

import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    user = input("Enter rock, paper, or scissors: ").strip().lower()

    if user not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.\n")
        return

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win! 🎉\n")
    else:
        print("You lose! 😢\n")

def main():
    print("Welcome to Rock, Paper, Scissors!\n")
    
    while True:
        play_round()
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
