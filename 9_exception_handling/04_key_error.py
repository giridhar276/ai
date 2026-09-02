employee = {"name": "Asha"}
try:
    print(employee["salary"])
except KeyError as error:
    print("Missing key:", error)
