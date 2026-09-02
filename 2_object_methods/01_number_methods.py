value = -12.75
print("Absolute:", abs(value))
print("Rounded:", round(value, 1))
print("Integer ratio:", value.as_integer_ratio())


number = 125
decimal_number = 12.75

# int methods
print("Binary representation:", number.bit_length())
print("Number of 1 bits:", number.bit_count())
print("125 as bytes:", number.to_bytes(2, byteorder="big"))
print("Integer ratio:", number.as_integer_ratio())

# float methods
print("Decimal ratio:", decimal_number.as_integer_ratio())
print("Is decimal an integer?:", decimal_number.is_integer())
print("Hexadecimal form:", decimal_number.hex())
print("Restored from hex:", float.fromhex(decimal_number.hex()))

# Related numeric built-in functions
print("Absolute value:", abs(-decimal_number))
print("Rounded value:", round(decimal_number, 1))
