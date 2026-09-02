filename = "courses.txt"
courses = ["Python\n", "SQL\n", "Excel\n"]
try:
    with open(filename, "w") as file:
        file.writelines(courses)
    print("Courses saved")
except OSError as error:
    print("File error:", error)
