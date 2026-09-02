numbers = [30, 10, 20]
numbers.append(40)
numbers.insert(1, 15)
numbers.remove(30)
numbers.sort()
print(numbers)
print("Removed:", numbers.pop())


courses = ["Python", "SQL", "Excel"]
print("Original list:", courses)

courses.append("Power BI")
print("After append():", courses)

courses.extend(["Pandas", "NumPy"])
print("After extend():", courses)

courses.insert(1, "Git")
print("After insert():", courses)

courses.remove("Excel")
print("After remove():", courses)

removed_course = courses.pop()
print("pop() returned:", removed_course)
print("After pop():", courses)

print("index('SQL'):", courses.index("SQL"))
print("count('Python'):", courses.count("Python"))

courses.sort()
print("After sort():", courses)

courses.reverse()
print("After reverse():", courses)

backup_courses = courses.copy()
courses.clear()
print("After clear():", courses)
print("Copied list:", backup_courses)
