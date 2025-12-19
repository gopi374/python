
#types of inheritance - 
# single inheritance
class bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class model(bike):
   pass 
m=model("hero","blue")
print(m.name,m.color)



# multi-level inheritance
 
class car():
    @staticmethod
    def start():
        print("car started")
        
    def stop():
        print("car stopped")
        
class toyota(car):
    def __init__(self,brand_name):
        self.brand_name=brand_name
        
class fortuner(toyota):
    def __init__(self,type):
        self.type=type
car1=fortuner("diesel")
car1.start()

# multiple inheritance

class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class c(A, B):
    varC="welcome to class c"
    
car=c()
print(car.varA)

