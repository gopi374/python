import random 

chars = "QWERTY1UI2OPAS5DFG3HJKL7ZXC8VBN0Mqw6erty4uiop2asdfgh0@jklzxcvbnm~!@#$%^&*()_:{<?>/.,;'][/*-+890}"
length = int (input("Enter the length of password :"))
password =""

for i in range(length):
    password+=random.choice(chars)
print("password is :",password)