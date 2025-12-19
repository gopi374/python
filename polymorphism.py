# polymorphism : oprator overloading 
# when the same operator is allowed to have different 
# meaning according to the context 

## program for adding or subtracting complex number


class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def shownumber(self):
        print(self.real,"i - ",self.img,"j")
        
    ''' def __add__(self,num2):
        newreal= self.real + num2.real
        newimg= self.img + num2.img
        return complex(newreal, newimg)'''
        
    def __sub__(self,num1):
        newreal= self.real - num1.real
        newimg= self.img - num1.img
        return complex(newreal, newimg)
        
num1=complex(int(input("Enter the 1st real number ")),int(input("Enter the 1st imaginary number ")))
num2=complex(int(input("Enter the 2nd real number ")),int(input("Enter the 2nd imaginary number ")))
num1.shownumber()
num2.shownumber()
mum3=num1-num2
mum3.shownumber()