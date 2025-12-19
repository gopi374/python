#break : if we use break operator in condition then it break the sentence immidiatly.
i=1
while i<=5:
    print(i)
    if (i==4):
        break                         
    i+=1
print("End of loop")


def tuple():
    num=(1,20,15,46,59,82,73,95)
    i=0
    x=82
    while i<len(num):
        if(num[i] == x):
            print(" x is found at index",i)
            break
        else:
            print("finding...")
        i+=1
