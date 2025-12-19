#create account class with 2 attributes= balance & account no.
#create methods for debit ,credit & printing the balance
class Account:
    def __init__(self,name,bal,acc):
        self.balance=bal
        self.name=name
        self.account_no=acc
    
    #debit
    def debit(self, amount):
        self.balance -= amount
        print(self.name,":",amount,"Rs is debited from your account")
        print("Total Balance is :",self.balance)
    #credit
    def credit(self, amount):
        self.balance += amount
        print(self.name,":",amount,"Rs is credited to your account")
        print("Total Balance is :",self.balance)
           
    
a1=Account("gopi",10000,12569954534)
a2=Account("Rahul",15698.2,1958612534)
a3=Account("Aman",15395.0,1853646534)
a4=Account("jack",183.295,111245565)

a1.credit(1000)
a1.debit(90.5)
a2.credit(1000)
a2.debit(893.5)
a3.debit(15399.5)
a4.debit(5964.5)
