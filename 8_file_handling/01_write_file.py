filename = "notes.txt"
mode = "w"
try:
    with open(filename, mode) as file:
        file.write("Python file handling is simple.\n")
    print("File written successfully")
except OSError as error:
    print("File error:", error)
