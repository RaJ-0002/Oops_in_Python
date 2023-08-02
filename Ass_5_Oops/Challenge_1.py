# Challenge 1: Square Numbers and Return Their Sum

class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sum = self.x**2+self.y**2+self.z**2
        return sum

a=float(input("Enter the 1st number"))
b=float(input("Enter the 2nd number"))
c= float(input("Enter the 3rd number"))

p1 = Point(a,b,c)
print("Sum of squares : ",p1.sqSum())