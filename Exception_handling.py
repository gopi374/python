
#      #ZeroDivisionError
try:
    num= input("enter a number ")
    result = 10 / int(num)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The result is: {result}")
    

  #key Error
dic={1:"gopi",2:"sai",3:"myname"}
try:
    num=int(input("Enter the key to search :"))
    print(dic[num])
except KeyError:
    print("Key not found in the dictionary!")
else:
    print(f"Key found : {dic[num]}")
    

   
    #IndexError
list1=[1,2,3,4]
try:
    num=int(input("enter the index number "))
    print(list1[num])
except IndexError:
    print("this index is not belongs to the list!")
else:
    print(f"the value at index {num} is : {list1[num]}")
    
    
    #ValueError
try:
    num=int(input("enter a number "))
except ValueError:
    print("please enter a valid value!")
else:
    print("you have enter the right value  !!")
    print("type of value :",type(num))
    
    #TypeError      
'''try:
    print("hello"+1)
except TypeError:
    print("please enter a valid number!")'''
    
