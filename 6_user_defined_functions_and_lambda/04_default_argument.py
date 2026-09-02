def calculate_price(price, tax_rate=0.18):
    return price + price * tax_rate

print(calculate_price(1000))
print(calculate_price(1000, 0.05))
