# Mad libs Python Project

def mad_libs():
    print("Let's play Mad Libs! Fill in the blanks below:\n")

    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    exclamation = input("Enter an exclamation: ")
    place = input("Enter a place: ")
    noun = input("Enter a noun: ")

    print("\nHere's your Mad Libs story:\n")
    print(f"One day, a {adjective} {animal} was walking through the forest.")
    print(f"It decided to {verb} near a tree when suddenly it heard a loud '{exclamation}!'")
    print(f"It ran as fast as it could and hid behind a {noun} in {place}.")
    print("The end!")

if __name__ == '__main__':
    mad_libs()
