# Countdown Timer

import time

def countdown(seconds):
    print(f"\nStarting countdown for {seconds} seconds:\n")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Overwrite the line each second
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")

def main():
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown(total_seconds)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
