employee = {"name": "Asha", "role": "Analyst"}
print(employee.keys())
print(employee.values())
print(employee.items())
print(employee.get("location", "Not available"))
employee.update({"location": "Pune"})
print(employee)


employee = {"id": 101, "name": "Asha", "role": "Analyst"}
print("Original dictionary:", employee)

print("keys():", employee.keys())
print("values():", employee.values())
print("items():", employee.items())
print("get('name'):", employee.get("name"))
print("get() with default:", employee.get("location", "Not assigned"))

employee.update({"location": "Hyderabad", "active": True})
print("After update():", employee)

employee.setdefault("department", "Data and AI")
employee.setdefault("role", "Developer")
print("After setdefault():", employee)

removed_role = employee.pop("role")
print("pop() returned:", removed_role)
print("After pop():", employee)

removed_item = employee.popitem()
print("popitem() returned:", removed_item)

employee_copy = employee.copy()
employee.clear()
print("After clear():", employee)
print("Copied dictionary:", employee_copy)

columns = ["Python", "SQL", "Excel"]
default_scores = dict.fromkeys(columns, 0)
print("fromkeys():", default_scores)
