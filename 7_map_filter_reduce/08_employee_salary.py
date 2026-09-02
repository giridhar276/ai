from functools import reduce

salaries = [30000, 45000, 55000, 70000]
revised = list(map(lambda salary: salary * 1.10, salaries))
high_salaries = list(filter(lambda salary: salary >= 50000, revised))
total = reduce(lambda a, b: a + b, high_salaries, 0)
print(revised)
print(high_salaries)
print(total)
