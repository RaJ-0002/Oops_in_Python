import json

class Employee:
    def __init__(self,Name,DOB,Height,City,State):
        self.Name=Name
        self.DOB = DOB
        self.Height = Height
        self.City = City
        self.State = State

with open("employee.json","r") as f:
    employee_data = json.load(f)

employee_list = list()

for employee_info in employee_data:
    employee = Employee(
        employee_info["Name"],
        employee_info["DOB"],
        employee_info["Height"],
        employee_info["City"],
        employee_info["State"]
    )
    employee_list.append(employee)

for employee in employee_list:
    print(f"Name: {employee.Name}, DOB: {employee.DOB}, Height: {employee.Height}, City: {employee.City}, State: {employee.State}")