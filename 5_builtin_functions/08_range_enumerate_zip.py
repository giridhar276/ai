names = ["Asha", "Ravi", "Meena"]
scores = [85, 90, 88]
for index, pair in enumerate(zip(names, scores), start=1):
    print(index, pair)
