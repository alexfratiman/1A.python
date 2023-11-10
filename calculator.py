x = float(input("Input first number: \n"))
y = float(input("Input second number: \n"))

print("Select an option to perform an operation: \n Add + \n Subtract - \n Multiply * \n Divide / \n Square s")

# This is how to do multiline strings
# print(
# '''

# ''')

operator = input()

if operator == "+":
    print("The result is:", x + y)
elif operator == "-":
    print("The result is:", x - y)
elif operator == "*":
    print("The result is:", x * y)
elif operator == "/":
    print("The result is:", x / y)
elif operator == "s":
    print("The first number squared is:", x * x)
else:
    print("Sorry, that is not an operator.")

