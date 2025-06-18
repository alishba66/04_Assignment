# Password Generator

import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password should be at least 6 characters for security.")
        return ""

    # Define character pools
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # special characters

    # Ensure the password has at least one of each
    all_chars = letters + digits + symbols
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest randomly
    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        user_length = int(input("Enter desired password length (min 6): "))
        password = generate_password(user_length)
        if password:
            print(f"🔐 Your generated password is:\n{password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
