# DICTIONARIES
# in other languate it might be called Has Table or Mab or Objects

dictionary = {"a": 1, "b": [1, 2, 3], "c": "gibson", "d": True}
# In dictionaries the key not change, its immutable
print(dictionary)

# Dictionary is a unorder kay value pair
print(dictionary["c"])

my_list = [
    {"a": 1, "b": [1, 2, 3], "c": "gibson", "d": True},
    {"a": 2, "b": [4, 5, 6], "c": "joseph", "d": False},
]
print(my_list[1]["b"][2])

user = {"basket": [1, 2, 3], "greet": "Hello gibbs"}
print(user.get("age", None))

new_user = dict(
    name="Joseph", age="24", job="Software developer"
)  # this way of creating dictionaries not common
print("new_user", new_user)

print("greet" in user.keys())  # If i want to check the key we can use the keys method
print(
    "Hello gibbs" in user.values()
)  # If i want to check the value we can use the values method


print(user.items())  # If i want to check the key we can use the keys method
# dict_items([('basket', [1, 2, 3]), ('greet', 'Hello gibbs')])

for key, value in user.items():
    print(f"{key}: {value}")

# user.clear()
# print(user)

new_user2 = new_user.copy()
print("new_user2", new_user2)

# print(new_user.pop("age", "10"))  # Pop return the vaue of whatever got removed
# print(new_user)

# print(
#     new_user.popitem()
# )  # this method is used to remove the last key:value from the dictionary
# print("After remove the last key:value", new_user)

new_user.update({"age": 89})
new_user.update(
    {"full_name": "Gibson joseph"}
)  # If the key does not exists it will still update the key as new key:value in the dic
print(new_user)
