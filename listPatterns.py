basket = ["a", "z", "b", "c", "d", "e", "f", "g", "d"]
basket.sort()
basket.reverse()
print(basket)

print(basket[::-1])  # Its also reverse the list and return the new list
print(basket)

# Range
# print(range(1, 100))
# print(list(range(1, 100)))
# print(list(range(0, 100)))

# Join
sentence = "!"
new_sentence = sentence.join(["I", "am", "gibson", "joseph"])
print(new_sentence)
