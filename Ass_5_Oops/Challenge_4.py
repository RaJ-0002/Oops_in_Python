# Challenge 4: Implement a Banking Account

class Account:
    
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance = balance

class SavingsAccount(Account):
    
    def __init__(self,title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

name = input("Enter the name of customer : ")
balance = float(input("Enter the initial deposite : "))
R = float(input("Enter the interest Rate on capital per anum : "))

# acc = Account("Ashish",5000)
# sa = SavingsAccount("Ashish",5000,5)

acc = Account(name,balance)
sa = SavingsAccount(name,balance,R)
print(acc.title)
print(acc.balance)
print(sa.title)
print(sa.balance)
print(sa.interestRate)
