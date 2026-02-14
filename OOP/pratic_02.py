''' 
Create a class Student with:
name
marks (list of numbers)
Methods:
calculate_total()
calculate_average()
Use @property to create:
grade (A, B, C based on average)
Example rule:
90+ → A
75+ → B
else → C
'''

class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)
    
    def calculate_average(self):
        return self.calculate_total() / len(self.marks)
    
    @property
    def grade(self):
        average = self.calculate_average()
        if average > 90:
            return "A"
        elif average > 75:
            return "B"
        else:
            return "C"
        
s1 = Student('Turkish',[99,90])
print(s1.calculate_total())
print(s1.calculate_average())
print(s1.grade)