def avg(a: float, b: float):
    total = a + b
    return total / 2

if __name__ == "__main__":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = avg(a, b)
    print("Average is:", result)
