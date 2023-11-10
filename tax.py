def getIncomeTax(salary):
    if salary <= 11850:
        return 0
    elif salary > 11850 and salary <= 34500:
        return (salary - 11850) * 0.2
    elif salary > 34500 and salary <= 150000:
        return (salary - 34500) * 0.4 + (34500 - 11850) * 0.2
    elif salary > 150000:
        return (salary - 150000) * 0.45 + (150000 - 34500) * 0.4 + (34500 - 11850) * 0.2

    
print(getIncomeTax(150001))