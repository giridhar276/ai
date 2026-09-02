filename = "notes.txt"
mode = "a"
try:
    with open(filename, mode) as file:
        file.write("This line was appended.\n")
    print("Text appended successfully")
except OSError as error:
    print("File error:", error)
