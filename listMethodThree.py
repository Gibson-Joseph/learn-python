basket = ["a", "x", "b", "c", "d", "e", "f", "g", "d"]
basket.reverse()
print(basket)

basket.sort()
print(sorted(basket, reverse=True))

new_basket = basket.copy()
new_basket.sort()
print(new_basket)

print(basket)
