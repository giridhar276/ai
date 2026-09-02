filename = "employees.txt"
try:
    with open(filename, "w") as file:
        file.write("Asha\nRavi\nMeena\n")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
except OSError as error:
    print("File error:", error)
