#Ex-1  class
class Student():
    name="gopi"

S1=Student()
print(S1.name)

#Ex-2
class Car:
    color="blue"
    brand="nano"

C1=Car()
print(C1.brand)
print(C1.color)


class person:   # class attributes
    def __init__(self, name, age):
        self.name = name   # object attributes
        self.age = age

class student(person):
    def __init__(self, name, age, total_marks):
        super().__init__(name, age)  # calling the parent class constructor
        self.total_marks = total_marks

    def display_info(self):
        print(f"student name= {self.name}")
        print(f"student age= {self.age}")
        print(f"student total_marks= {self.total_marks}")

p1 = student("user1", 20, 150)
p2 = student("user2", 22, 120)
p1.display_info()
print("=" * 20)
p2.display_info()


#3.constructor
class person:   #class attributes
    def __init__(self,name,age):
        self.name=name   #object attributes
        self.age=age

class student(person):
    def __init__(self,name,age,total_marks): #super keyword is used for inherit the property of parent class
        super().__init__(name,age)
        self.total_marks=total_marks

    def display_info(self):
        print(f"student name= {self.name}")
        print(f"student age= {self.age}")
        print(f"student total_marks= {self.total_marks}")
        print(f"Student grade = {self.calulate_grade()}")

    def calulate_grade(self):
        if self.total_marks < 90 and self.total_marks > 80:
            print("A+")
        elif(self.total_marks < 80 and self.total_marks > 70):
            print("A")
        elif(self.total_marks < 70 and self.total_marks > 60):
            print("B")
        elif(self.total_marks < 60 and self.total_marks > 50):
            print("C")
        else:
            print("fail")
       
p1=student("user1",18,50)
p2=student("user2",20,80)
p1.display_info()
print("="*20)
p2.display_info()


#method
class person2:     #class
    def __init__(self,name,scholar):     #constructor
        self.name=name
        self.scholar=scholar
    def hello(self):   #functions between class  called methods.
        print("the name is"+self.name)
    def scholar(self):
        return self.scholar
p2=person2(" gopi",12)  
p2.hello()
print(p2.scholar)