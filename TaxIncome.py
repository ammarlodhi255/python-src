def get_income_tax(income):
    if (income <= 10000): return 0
    elif(10000 < income <= 20000): return ((income - 10000) * (10/100))
    elif income > 20000: 
        return (10000*(10/100)) + ((income - 20000)*(25/100))

income = int(input("Enter your income please: "))
print(f"Your income tax is: {get_income_tax(income)}")