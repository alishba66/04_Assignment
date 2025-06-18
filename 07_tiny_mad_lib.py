Sentences_apart : str = ("Code in Place is fun. I learned to program and used Python to make my")



def main():
    print("Delete this line and write your code here! :)")
    Adjective : str = str (input("Enter any adjective for the sentence."))
    Noun : str =  str(input("Enter a noun for the sentence."))
    Verb : str = str (input("Enter a verb for the sentence."))
    print(str(Sentences_apart) + " " + str(Adjective) + " " +str(Noun) + " " + str(Verb))


if __name__ == '__main__':
    main()