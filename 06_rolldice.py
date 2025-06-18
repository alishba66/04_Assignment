import random

dice_sides = 6

def main():
    print("die1 and die2 and its sum! :)")
    die1 : int = random.randint(1, dice_sides)
    die2 : int = random.randint(1, dice_sides)
    total = die1 + die2
    print(f"{die1} die1")
    print(f"{die2} die2")
    print(f"The sum of die1 and die2 is: {total}")


if __name__ == '__main__':
    main()