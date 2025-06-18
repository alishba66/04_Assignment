import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generates and prints N_NUMBERS random integers between MIN_VALUE and MAX_VALUE.
    """
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)
        print(num, end=' ')
    print()  

if __name__ == '__main__':
    main()
