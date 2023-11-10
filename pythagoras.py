print("Pythagoras' Calculator. Select an option to continue: \n Enter '1' to Find the length of A given B and C \n Enter '2' to Find the length of B given A and C \n Enter '3' to Find the length of C given A and B")

selection = input()

if selection == "1":
    sideB = float(input("Please enter the length of side B: \n"))
    sideC = float(input("Please enter the length of side C: \n"))
    sideA = (sideC ** 2 - sideB ** 2) ** 0.5
    print("The length of side A is:", sideA)
elif selection == "2":
    sideA = float(input("Please enter the length of side A: \n"))
    sideC = float(input("Please enter the length of side C: \n"))
    sideB = (sideC ** 2 - sideA ** 2) ** 0.5
    print("The length of side B is:", sideB)
elif selection == "3":
    sideA = float(input("Please enter the length of side A: \n"))
    sideB = float(input("Please enter the length of side B: \n"))
    sideC = (sideB ** 2 + sideA ** 2) ** 0.5
    print("The length of side C is:", sideC)
else:
    print("Sorry, that is not an option.")

