# @static method is used for common method for a class.
# by super method 

class car():
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("car started")
        
    def stop():
        print("car stopped")
        
class toyota(car):
    def __init__(self,brand_name,type):
        super().__init__(type)
        self.brand_name=brand_name
        super().start()
        
car2=car("electric")
car1=toyota("gdgfhf","diesel")
print(car1.type,car1.start())
