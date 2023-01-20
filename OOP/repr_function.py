class Employee():
    def __init__(self, firstname, lastname, email, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.gender = gender

    def __repr__(self):
        gender = self.gender.lower()
        info = ''
        if gender == 'male':
            info = f'Mr. {self.firstname} {self.lastname}'
        else:
            info = f'Miss {self.firstname} {self.lastname}'

        return info


emp_1 = Employee('Ammar', 'Ahmed', 'ammar@gmail.com', 'Male')
print(emp_1)
