
proceed = True


while (proceed):
    number = int(input("Please enter a number:\n"))
    factorial = 1
    i = 1
    while i <= number:
        factorial = factorial * i
        i += 1
    print("The factorial is:", factorial)

    flag = True
    while flag:
        choice = input("Do you want to calculate another factorial? y or n\n")
        if choice == "n":
            flag = False
            proceed = False
        elif choice ==  "y":
            flag = False
        else:
            print("That is not a valid option, please try again.")






    
