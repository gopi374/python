def age_classifier():
    name=input("Enter your name sir :")
    a=int(input("Enter your age :"))
    if a<=1:
        print("you are infant")
    elif a>=1 and a<=13:
        print("you are child")
    elif a>=14 and a<=20:
        print("you are teenager")
    elif a>20:
        print("you are adult")
   
