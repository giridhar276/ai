import sys

# Python runtime information
print("Python version:", sys.version)
print("Version details:", sys.version_info)
print("Operating-system platform:", sys.platform)
print("Python executable:", sys.executable)
print("Implementation:", sys.implementation.name)

# Command-line arguments: python 02_sys_module.py input.txt 10
print("Complete argument list:", sys.argv)
print("Script name:", sys.argv[0])
if len(sys.argv) > 1:
    print("Arguments supplied by user:", sys.argv[1:])
else:
    print("No additional command-line arguments supplied")

# Module search locations
print("First module search path:", sys.path[0])
print("Number of search locations:", len(sys.path))

# Loaded modules
print("Is os already loaded?:", "os" in sys.modules)
print("Number of loaded modules:", len(sys.modules))

# Object size and reference information
sample_data = [10, 20, 30, 40]
print("Object size in bytes:", sys.getsizeof(sample_data))
print("Maximum integer size:", sys.maxsize)
print("Default text encoding:", sys.getdefaultencoding())

# Standard output and standard error
sys.stdout.write("Message written with sys.stdout.write()\n")
sys.stderr.write("Demonstration message from sys.stderr.write()\n")
