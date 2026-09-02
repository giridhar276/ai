filename = "number.txt"
try:
    with open(filename, "w") as file:
        file.write("125")
    with open(filename, "r") as file:
        number = int(file.read())
    print("Double:", number * 2)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("The file does not contain a valid number")
except OSError as error:
    print("File error:", error)
