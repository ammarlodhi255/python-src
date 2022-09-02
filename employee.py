class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_of_emps += 1 # You wouldn't want to use 'self' keyword here. WHY?
        
    def income_tax(self):
        return ((10/100) * self.pay)

    def fullname(self):
        return f'{self.first} {self.last}'

    def email(self):
        return f'{first}.{last}@company.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

if __name__ == "__main__":
    emp1 = Employee('Ammar', 'Ahmed', 25, 100000)
    print(f'Income Tax is: {emp1.income_tax()}')

    print(emp1.pay)
    emp1.raise_amount = 1.07
    emp1.apply_raise()
    print(emp1.pay)
    print(emp1.raise_amount)

    print(f'Accessing the Employee class variable {Employee.raise_amount}')
    print(emp1.__dict__)