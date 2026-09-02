values = (10, 20, 10, 30, 10)
print("Count of 10:", values.count(10))
print("Index of 20:", values.index(20))


scores = (82, 91, 76, 82, 88, 82)
print("Tuple:", scores)

# A tuple has only two public methods: count() and index().
print("count(82):", scores.count(82))
print("index(91):", scores.index(91))

# Tuple operations that do not modify the tuple
print("First score:", scores[0])
print("Last score:", scores[-1])
print("First three scores:", scores[:3])
print("Tuple length:", len(scores))
print("Minimum score:", min(scores))
print("Maximum score:", max(scores))
print("Total score:", sum(scores))

# Tuple unpacking
employee = (101, "Asha", "Developer")
employee_id, employee_name, role = employee
print("Unpacked values:", employee_id, employee_name, role)

# Extended unpacking
first, *middle, last = scores
print("First:", first)
print("Middle:", middle)
print("Last:", last)
