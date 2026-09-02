import math

# Constants
print("Pi:", math.pi)
print("Euler's number:", math.e)
print("Infinity:", math.inf)

# Rounding and absolute values
print("Floor:", math.floor(12.9))
print("Ceiling:", math.ceil(12.1))
print("Truncate:", math.trunc(-12.9))
print("Absolute value:", math.fabs(-25.5))

# Powers and logarithms
print("Square root:", math.sqrt(81))
print("Integer square root:", math.isqrt(80))
print("2 raised to power 5:", math.pow(2, 5))
print("Natural logarithm:", math.log(math.e))
print("Base-10 logarithm:", math.log10(1000))
print("Exponential:", math.exp(2))

# Number theory
print("Factorial:", math.factorial(5))
print("Greatest common divisor:", math.gcd(24, 36))
print("Least common multiple:", math.lcm(8, 12))
print("Combinations:", math.comb(5, 2))
print("Permutations:", math.perm(5, 2))

# Trigonometry uses radians
angle_degrees = 30
angle_radians = math.radians(angle_degrees)
print("Radians:", angle_radians)
print("Sine:", math.sin(angle_radians))
print("Cosine:", math.cos(angle_radians))
print("Back to degrees:", math.degrees(angle_radians))

# Accuracy and validation helpers
print("Hypotenuse:", math.hypot(3, 4))
print("Values are close:", math.isclose(0.1 + 0.2, 0.3))
print("Is finite:", math.isfinite(100.0))
