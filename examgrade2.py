examMark = int(input("Please input your exam mark: \n"))
studentLevel = int(input("Please input your student level: \n"))

if studentLevel == 1:
    if examMark < 50:
        print("Your grade is: Fail")
    elif examMark >= 50 and examMark <= 60:
        print("Your grade is: Pass")
    elif examMark >= 61 and examMark <= 70:
        print("Your grade is: Merit")
    elif examMark >= 71 and examMark <= 100:
        print("Your grade is: Distinction")
    else:
        print("Error: marks must be between 1..100")
elif studentLevel == 2:
    if examMark < 40:
        print("Your grade is: Fail")
    elif examMark >= 40 and examMark <= 50:
        print("Your grade is: Pass")
    elif examMark >= 51 and examMark <= 65:
        print("Your grade is: Merit")
    elif examMark >= 66 and examMark <= 100:
        print("Your grade is: Distinction")
    else:
        print("Error: marks must be between 1..100")
else:
    print("Error: Student level must be 1 or 2")

