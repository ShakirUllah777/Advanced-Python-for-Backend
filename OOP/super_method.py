'''
super() is used to call methods or constructor of the parent class from the child class.
It allows the child class to reuse and extend the parent class functionality.
'''

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print("Vehicle constructor called")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   
        self.model = model
        print("Car constructor called")

c = Car('Toyota', 'ABC')
print(c.brand)
print(c.model)

