# single inheritnace 
class Car:
    @staticmethod
    def start():
        print('Car started...')

    @staticmethod
    def stop():
        print('Car stoped...')

class TeslaCar(Car):
    def __init__(self, name):
        self.name = name

c1 = TeslaCar('Tesla1')
print(c1.name)
print(c1.start())
print(c1.stop())


# Multilevel Inheritance 
class Vehicle:
    def start(self):
        print('Car started...')

class Car(Vehicle):
    def music(self):
        print('Music started..')

class ElectricCar(Car):
    def battery(self):
        print('Battery is Full...')


e = ElectricCar()
e.start()
e.music()
e.battery()

# Multiple inheritance
class Camera:
    def click(self):
        print("Photo clicked")

class MusicPlayer:
    def play_music(self):
        print("Playing music")

class Smartphone(Camera, MusicPlayer):  # inherits both
    def make_call(self):
        print("Calling...")

s = Smartphone()
s.click()        
s.play_music()   
s.make_call()    
