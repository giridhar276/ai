age = 15
try:
    if age < 18:
        raise ValueError("Age must be at least 18")
    print("Registration allowed")
except ValueError as error:
    print(error)
