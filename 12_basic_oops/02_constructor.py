class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(self.name, "-", self.role)

employee = Employee("Asha", "Analyst")
employee.display()
