string = input("please input a word:\n")
vowels = ['a','e','i','o','u']
vowelNumber = 0

for i in string:
    if i in vowels:
        vowelNumber += 1

print("there are",vowelNumber, "vowels in your word")