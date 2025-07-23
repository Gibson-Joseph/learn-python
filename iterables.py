# Iterables:
# iterable can be a list, dictionary, tuple, set, string
# iterated -> one by one to check each item in the collection.

for item in {1, 2, 3, 4, 5}:
    for x in ["a", "b", "c"]:
        print(item, ":", x)

# DOUBT: HOW DO THE FOLLOWING TWO PRINTS WORKS??
print(item)
print(x)


user = {"name": "Gibson", "age": 24, "can_swim": False}

for item in user:
    # We can print the key of the dictionary
    print("Dictionary item key:", item)
    print("Dictionary item value:", user[item])
    # Dictionary item: name
    # Dictionary item: age
    # Dictionary item: can_swim

print("Items part #1")
for item in user.items():  # we can get the tuple
    print(item)
    # ('name', 'Gibson')
    # ('age', 24)
    # ('can_swim', False)
    # we can unpack the tuple like the following:
    key, value = item
    print(f"{key}:{value}")

print("Items part #2")
for key, value in user.items():
    print(f"{key}:{value}")

print("Values")
for item in user.values():  # This gives us the value of the dictionaries
    print(item)
    # Gibson
    # 24
    # False

print("Keys")
for item in user.keys():  # This gives us the key of the dictionaries
    print(item)
    # name
    # age
    # can_swim
