filename = "notes.txt"
mode = "r"
try:
    with open(filename, mode) as file:
        print(file.read())
except FileNotFoundError:
    print("Create notes.txt first by running 01_write_file.py")
