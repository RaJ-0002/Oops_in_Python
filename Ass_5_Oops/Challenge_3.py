# Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self):
        pass

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

    def getRollNumber(self):
        return self._rollNumber

student = Student()

name = input("Enter student name: ")
rollNumber = input("Enter student roll number: ")

student.setName(name)
student.setRollNumber(rollNumber)

print("Name:", student.getName())
print("Roll Number:", student.getRollNumber())
