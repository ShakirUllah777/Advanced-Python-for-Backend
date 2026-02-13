# Class method
class Person:
    name = 'harry'

    @classmethod #this help to chnage the overall name , also the default name
    def chnageName(cls,name):
        cls.name = name

p = Person()
p.chnageName('Malik')
print(p.name)
print(Person.name)



# @property metod -- used class as instance
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(5, 4)
print(r.area)
