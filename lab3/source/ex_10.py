def calculate_price(price, discount=0.1):
    return price * (1 - discount)

print(f"Price after discount: {calculate_price(100)}")
print(f"Price after discount: {calculate_price(1000, 0.5)}")