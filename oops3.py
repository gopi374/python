# private and public methods of python(oops)
# private : by adding _ _ at method and attributes.
# private attributes & mathods are meant to be used only within the class
# and are not accessible from outside the class.

class account:
    def __init__(self,acc_no,password):
        self.acc_no=acc_no
        self.__password=password
    def to_show_private_things(self):
        print(self.__password)
a1=account(12345,"sffijodu")
print("password is ",a1.to_show_private_things())


class person:
    __name="gopi"
    
    def __hello(self):
        print(self.__name)
    def welcome(self):
        self.__hello()
        
p1=person()
print(p1.welcome())
