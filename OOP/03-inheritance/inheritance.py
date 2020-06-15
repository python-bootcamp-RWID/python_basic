class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self):
        print(f'My name is : {self.name}, My Age is : {self.age}')


class Student(Person):
    pass


# membuat instansiasi object
student1 = Student("Danil", 26)
student2 = Student("Haykal", 20)

student1.printDetails()
student2.printDetails()
