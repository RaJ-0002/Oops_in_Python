# Challenge 2: Implement a Calculator Class

class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        return self.num1+self.num2

    def subtract(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2
    
num1=float(input("Enter the 1st number"))
num2=float(input("Enter the 2nd number"))

cal = Calculator(num1,num2)

print("Sum ------------>:",cal.add())
print("Subtraction ---->:",cal.subtract())
print("Multiplication ->:",cal.multiply())
print("Division ------->:",cal.divide())