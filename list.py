# List is the order sequence of object, that can be a any type data.
# sting slicing:
string = "hello"
# print(string[0:2:1]) # start: stop: step

amazon_cart = ["notebook", "sunglasses", "toys", "grapes"]

# List slicing
print(amazon_cart)  # Get every single item from the cart
print(amazon_cart[0::2])

print("-" * 50)
amazon_cart[0] = "laptop"
new_cart = amazon_cart[:]
# [:] this will help you to copy the all items from the original list

new_cart[0] = "gum"

print(new_cart)  # list slicing will creating a new list
print(amazon_cart)
