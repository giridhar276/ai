filename = "employees.csv"
try:
    with open(filename, "w") as file:
        file.write("id,name,department\n101,Asha,IT\n102,Ravi,HR\n")
    with open(filename, "r") as file:
        print(file.read())
except OSError as error:
    print("File error:", error)
