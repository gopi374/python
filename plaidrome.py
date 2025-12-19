def palindrom():
    string=input("enter the string :")
    if string == string[::-1]:
        print("string is palindrome ")
    else:
        print("stirng is not palindrome")

palindrom()
