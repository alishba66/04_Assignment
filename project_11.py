# Binary Search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found at index mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found

def main():
    arr = sorted([12, 25, 31, 47, 53, 68, 79, 88, 95])
    print("Sorted List:", arr)
    target = int(input("Enter the number to search for: "))

    result = binary_search(arr, target)
    if result != -1:
        print(f"{target} found at index {result}.")
    else:
        print("Number not found.")

if __name__ == "__main__":
    main()
