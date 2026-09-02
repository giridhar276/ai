numbers = [1, 2, 3, 4, 5, 6]
even_squares = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers)))
print(even_squares)
