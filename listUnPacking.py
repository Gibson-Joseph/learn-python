# List Unpacking
basket = [1, 2, 3]
# basket = 1, 2, 3
print(basket)

a, b, c = basket
print(a)
print(b)
print(c)

print("-" * 100)

new_basket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

a, b, c, *others, d, e = new_basket
print(a)
print(b)
print(c)
print(others)
print(d)
print(e)
