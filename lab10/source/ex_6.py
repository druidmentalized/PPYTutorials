def calculate_total(cart):
    final_price = 0.
    for price in cart.values():
        final_price += price if price < 50 else price * 0.95

    if final_price > 100:
        final_price = final_price * 0.9

    return final_price


test_cart = {
    'laptop': 900,
    'mouse': 25,
    'keyboard': 45
}

print(calculate_total(test_cart))