import random

# Use seed() when repeatable results are needed for testing
random.seed(42)

print("Random float from 0 to 1:", random.random())
print("Random integer, inclusive:", random.randint(1, 100))
print("Random integer using range rules:", random.randrange(10, 101, 10))
print("Random floating-point value:", random.uniform(1.5, 9.5))

courses = ["Python", "SQL", "Excel", "Power BI", "Cloud"]
print("One random course:", random.choice(courses))
print("Three choices with repetition:", random.choices(courses, k=3))
print("Three unique courses:", random.sample(courses, k=3))

random.shuffle(courses)
print("Shuffled courses:", courses)

# Weighted selection
ratings = ["Excellent", "Good", "Average"]
weights = [0.5, 0.35, 0.15]
print("Weighted feedback:", random.choices(ratings, weights=weights, k=5))

# Random bytes and common probability distributions
print("Random bytes:", random.randbytes(5))
print("Normal distribution value:", random.gauss(mu=70, sigma=10))
