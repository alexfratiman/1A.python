examMark = int(input("Please input your exam mark, 1-100: \n"))

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

