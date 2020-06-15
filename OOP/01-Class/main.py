# class MyClass():
#     pass
#
# class1 = MyClass()
# class2 = MyClass()
#
# print(class1)
# print(class2)


class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

emp1.firstName = 'danil'
emp1.email = 'danil@gmail.com'
emp1.salary = 3000

emp2.firstName = 'haykal'
emp2.email = 'haykal@gmail.com'
emp2.salary = 5000

print(f'your first name :{emp1.firstName}')
print(f'your email :{emp1.email}')
print(f'your salary :{emp1.salary}')

print(f'your first name :{emp2.firstName}')
print(f'your email :{emp2.email}')
print(f'your salary :{emp2.salary}')

salaryTotal = emp1.salary + emp2.salary
print(salaryTotal)
