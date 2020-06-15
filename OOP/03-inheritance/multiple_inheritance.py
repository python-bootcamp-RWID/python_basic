class Person:
    def __init__(self):
        print('Please Enter Your Details')
        self.name = input('Enter name :')
        self.lname = input('Enter last name :')
        self.phone = input('Enter Phone :')
        self.age = input('Enter Age :')

    def PrintDetails(self):
        print(f'\n\nName            : {self.name}')
        print(f'Lastname       : {self.lname}')
        print(f'Phone Number   : {self.phone}')
        print(f'Age            : {self.age}')


class StudentMarks:
    def __init__(self):
        print("Please Enter Your Marks")
        self.math = int(input("Math mark : "))
        self.history = int(input("History mark :"))
        self.programming = int(input("Programming mark :"))

    def PrintDetails(self):
        totalExamMarks = self.math + self.history + self.programming

        if totalExamMarks < 80:
            print("Total Exam Marks     : ", str(totalExamMarks))
            print("Your Failed")
        else:
            print(f"Total Exam Marks    : {str(totalExamMarks)}")
            print("You are succeessed")


class Student(Person,StudentMarks):
    def __init__(self):
        Person.__init__(self)
        StudentMarks.__init__(self)

    def PrintResult(self):
        Person.PrintDetails(self)
        StudentMarks.PrintDetails(self)


student1 = Student()
student1.PrintResult()