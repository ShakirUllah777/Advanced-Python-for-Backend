''' Create student class that take name and marks of 3 subject 
as argument in constructor.
then Create a method to print the average '''


class Student():
    def __init__(self, name , marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        sum_num = self.marks1 + self.marks2 + self.marks3
        percent = sum_num / 3
        return f'Hi {self.name} Your Average Marks is {percent} '
    

s1 = Student('harry', 60,21,33)
print(s1.average())