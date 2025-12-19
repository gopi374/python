# del Keyword : it is used for deleting object or class attribute.
class shradha:
    def __init__(self,name):
        self.name=name
        
s1=shradha("gopi")
print(s1.name)

# Question no. 2
class Account:
    def __init__(self,acc_no,password):
        self.account_no=acc_no
        self.__password=password
    #
    def reset(self):
        print(self.__password)
a1=Account(125364,"abcde")
print(a1.account_no)
print(a1.reset())