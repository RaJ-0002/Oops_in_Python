# Challenge 5: Handling a Bank Account

class Account:
    
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self,wd):
        self.balance -= wd
    
    def deposit(self,depo):
        self.balance += depo
    
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    
    def __init__(self,title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        self.interest = (self.interestRate*self.balance)/100
        return self.interest
        


demo1 = SavingsAccount("Ashish",5000,5)

print("Before deposite",demo1.getBalance())
depo = float(input("Enter the amonut to deposit : "))
demo1.deposit(depo)


print("After deposite : ",demo1.getBalance())
wd = int(input("Enter amount for withdrawal : "))
demo1.withdrawal(wd)
print(f"After withdrawal of {wd} is ",demo1.getBalance())

print("Interest on capital amount is ",demo1.interestAmount())