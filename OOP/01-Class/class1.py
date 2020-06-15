class Employee:
    def fullName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

        print(firstName +" "+ lastName)

emp1 = Employee()
emp1.fullName('danil', 'syah arihardjo')

emp2 = Employee()
emp2.fullName('haykal','dafiansyah')