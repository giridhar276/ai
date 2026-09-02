class Employee:
    def role(self):
        print("General employee")

class Developer(Employee):
    def role(self):
        print("Software developer")

employee = Developer()
employee.role()
