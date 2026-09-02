from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda first, second: first * second, numbers)
print(product)
