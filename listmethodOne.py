# List method part 1
basket = [1, 2, 3, 4, 5]
# print(len(basket))

# ADDING
# Everything in python is object: number is object, list is object
basket.append(100)
basket.insert(2, 200)
basket.extend([300, 400])
# new_list = basket
# print("basket", basket)
# print("new_list", new_list)

# REMOVING
print("before removing", basket)
basket.pop()
basket.pop(0)
basket.remove(4)  # Its remove the value
basket.clear()  # Clear remove whatever in the list (copmletely clear the list)
print("after removing", basket)
