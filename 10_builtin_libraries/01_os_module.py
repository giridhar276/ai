import os
from pathlib import Path

# 1. Current working directory
print("Current working directory:", os.getcwd())

# 2. List files and folders
print("Items in current directory:", os.listdir("."))

# Use a safe demonstration folder
demo_folder = "os_demo"
nested_folder = os.path.join(demo_folder, "reports", "2026")

# 3. Create one or many directories
os.makedirs(nested_folder, exist_ok=True)
print("Created directory:", nested_folder)

# 4. Build paths in an operating-system-independent way
file_path = os.path.join(nested_folder, "sales.txt")
print("Joined path:", file_path)

# Create a sample file for the remaining operations
with open(file_path, "w") as file:
    file.write("January: 125000\nFebruary: 143000\n")

# 5. Test whether paths exist and identify their type
print("Path exists:", os.path.exists(file_path))
print("Is a file:", os.path.isfile(file_path))
print("Is a directory:", os.path.isdir(nested_folder))

# 6. Extract path components
print("Absolute path:", os.path.abspath(file_path))
print("File name:", os.path.basename(file_path))
print("Parent directory:", os.path.dirname(file_path))
print("Name and extension:", os.path.splitext(file_path))

# 7. Read file information
print("File size in bytes:", os.path.getsize(file_path))
print("Last modified timestamp:", os.path.getmtime(file_path))

# 8. Rename a file
renamed_path = os.path.join(nested_folder, "monthly_sales.txt")
os.rename(file_path, renamed_path)
print("Renamed file exists:", os.path.exists(renamed_path))

# 9. Work with environment variables
os.environ["TRAINING_BATCH"] = "PYTHON-SEP-2026"
print("Environment variable:", os.getenv("TRAINING_BATCH"))
print("Missing variable with default:", os.getenv("UNKNOWN_KEY", "Not configured"))

# 10. Walk through a directory tree
for root, directories, files in os.walk(demo_folder):
    print("Walk root:", root)
    print("Subdirectories:", directories)
    print("Files:", files)

# 11. Remove the sample file and empty directories
os.remove(renamed_path)
os.removedirs(nested_folder)
print("Cleanup completed:", not Path(demo_folder).exists())
