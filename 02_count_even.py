def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    count = 0  
    for num in lst:  
        if num % 2 == 0:  
            count += 1 
    return count

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  
    user_input = input("Enter an integer or press enter to stop: ")  
    while user_input != "":  
        try:
            lst.append(int(user_input))  
        except ValueError:
            print("Invalid input. Please enter an integer.")
        user_input = input("Enter an integer or press enter to stop: ")  
    return lst

def main():
    lst = get_list_of_ints()
    result = count_even(lst)
    print(f"Number of even numbers: {result}")

if __name__ == '__main__':
    main()
