source_filename = "source.txt"
target_filename = "target.txt"
try:
    with open(source_filename, "w") as file:
        file.write("Content to copy")
    with open(source_filename, "r") as source:
        content = source.read()
    with open(target_filename, "w") as target:
        target.write(content)
    print("Content copied")
except OSError as error:
    print("File error:", error)
