def add_numbers(numbers) -> int :
    total_so_far = 0
    for number in numbers:
        total_so_far =+ number
        
        return total_so_far
    
    
def main():
    numbers: list[int] = [ 99, 2, 3, 4, 7]
    sum_of_numbers:int = add_numbers(numbers)
    print(sum_of_numbers)
    
if __name__ == "__main__": 
   main()   