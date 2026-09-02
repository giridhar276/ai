courses = ["Python", "SQL"]
try:
    print(courses[5])
except IndexError:
    print("List position does not exist")
