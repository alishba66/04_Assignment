import random

def main():
    guess_num = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99.")

    guess = int(input("Enter a number: "))  

    while guess != guess_num:
        if guess < guess_num:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        guess = int(input("Enter a new guess number: "))

    print("Congrats! Your guess is correct. The number was " + str(guess_num))

if __name__ == "__main__":
    main()