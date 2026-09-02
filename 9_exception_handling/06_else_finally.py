try:
    number = int("25")
except ValueError:
    print("Invalid number")
else:
    print("Valid number:", number)
finally:
    print("Validation finished")
