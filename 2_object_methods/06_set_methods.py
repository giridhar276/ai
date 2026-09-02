python_students = {"Asha", "Ravi", "John"}
sql_students = {"Ravi", "Meena", "John"}
print("Both:", python_students.intersection(sql_students))
print("All:", python_students.union(sql_students))
print("Only Python:", python_students.difference(sql_students))


python_students = {"Asha", "Ravi", "John", "Meena"}
sql_students = {"Ravi", "Meena", "Kiran"}
print("Python students:", python_students)
print("SQL students:", sql_students)

python_students.add("Divya")
print("After add():", python_students)

python_students.update(["Anil", "Sara"])
print("After update():", python_students)

print("union():", python_students.union(sql_students))
print("intersection():", python_students.intersection(sql_students))
print("difference():", python_students.difference(sql_students))
print("symmetric_difference():", python_students.symmetric_difference(sql_students))

python_copy = python_students.copy()
python_copy.intersection_update(sql_students)
print("After intersection_update():", python_copy)

python_students.discard("John")
print("After discard():", python_students)

python_students.remove("Asha")
print("After remove():", python_students)

removed_student = python_students.pop()
print("pop() returned:", removed_student)

required_skills = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "Excel"}
print("issubset():", required_skills.issubset(candidate_skills))
print("issuperset():", candidate_skills.issuperset(required_skills))
print("isdisjoint():", {"Java"}.isdisjoint(required_skills))
