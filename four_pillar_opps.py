#four pillars of object oriented programming in python
#1.Abstraction-HIding the unneccesary details of working class And showing only essential things to user.
#2.Encapsulation - Wrapping data and functions into in a single unit.
#3. inheritance - inherit some properties/ methods from parent class 
#4. polymorphism - Means many forms


# Example of Abstraction
class car:
    print("hello world")
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.acc=True
        self.brk=True
        print("car started")
c1=car()
c1.start()
        
# Examplle of inheritance 
class Hyundai(car):
    super@__init__