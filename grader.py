import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",")
grades = list(map(int, grades))

print("The minimum value is {} and the maximum is {}".format(min(grades), max(grades)))

gradesAvg = round(sum(grades) / len(grades), 2)
print("The grades average is", gradesAvg)

print("The grades mean is", round(statistics.mean(grades), 2))
print("The grades median is", round(statistics.median(grades), 2))

print("The grades have an average value of {}, minimum of {}, maximum of {}, mean of {}, and median of {}.".format(gradesAvg, min(grades), max(grades), round(statistics.mean(grades),2), round(statistics.median(grades), 2)))







