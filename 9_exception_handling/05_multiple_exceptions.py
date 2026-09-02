value = "0"
try:
    result = 100 / int(value)
    print(result)
except ValueError:
    print("Value must be numeric")
except ZeroDivisionError:
    print("Value must not be zero")
