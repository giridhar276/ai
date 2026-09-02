class Employee:
    company = "ABC Technologies"

    def __init__(self, name):
        self.name = name

first = Employee("Asha")
second = Employee("Ravi")
print(first.name, first.company)
print(second.name, second.company)
