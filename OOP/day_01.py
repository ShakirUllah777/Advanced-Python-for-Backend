# Basic of the OOP in Python 

# simple OOP 
class Car:
    name = 'Tesla'
    model = 2025

car1 = Car()
car2 = Car()
print(car1.name , car1.model)
print(car2.name, car2.model)

# Class using the instructor
class Student():
    college_name = 'Apna College'
    def __init__(self , name , age):
        self.name = name
        self.age = age

s1 = Student('Harry',23)
s2 = Student('Malik',21)
print(s1.name, s1.age , s1.college_name)
print(s2.name, s2.age, s1.college_name)


# Methods(function) in Class
class Person():
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def wellcome(self):
        print('WellCome,', self.name)

    def return_age(self):
        print("Years Old,",self.age)
    

p1 = Person('Turkish',23)
p1.wellcome()
p1.return_age()


