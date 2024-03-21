class Employee:
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = str(firstName.lower()) + '.' + str(lastName.lower()) + '@company.net'
    def full_name(self):
        return '{} {}'.format(self.firstName, self.lastName)

emp1 = Employee('John', 'Doe', 5000)
emp2 = Employee('Jeniffer', 'Mary', 6000)

print(Employee.full_name(emp1))