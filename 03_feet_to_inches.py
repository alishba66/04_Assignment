feet_to_inches : int = 12

def main():
    print("convert feet to inches! :)")
    feet: float = float (input("Enter a feet to convert into inches."))
    inches:float = feet * feet_to_inches
    print(f"{feet} feets = {inches} inches")
  



if __name__ == '__main__':
    main()