import random

Num_sides = 6  # Corrected variable name

def roll_dice():
    die1 = random.randint(1, Num_sides)  # Removed unnecessary type hints
    die2 = random.randint(1, Num_sides)
    total = die1 + die2
    print(f"The total of die1 and die2 is {total}.")  # Used f-string

def main():
    die1 = 10  # Removed unnecessary type hint
    print(f"die1 in main() starts as: {die1}")  # Used f-string
    
    roll_dice()
    roll_dice()
    roll_dice()
    
    print(f"die1 in main() is: {die1}")  # Used f-string

# Ensure main() runs only when this script is executed directly
if __name__ == '__main__':
    main()
