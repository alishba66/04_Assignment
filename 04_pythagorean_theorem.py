import math

def main():
    print("Find the hypotenuse of the Triangle! :)")
    AB: float = float(input("Enter a length of AB. "))
    AC: float = float(input("Enter a length of AC. "))
    BC: float = math.sqrt (AB**2 + AC**2)
    print(f"The hypotenuse of the Triangle is {BC}")
    

if __name__ == '__main__':
    main()