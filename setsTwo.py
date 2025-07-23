# difference()
# discard()
# difference_update()
# intersection()
# isdisjoint()
# issubset()
# issuperset()
# union()

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print("my_set", my_set)
print("your_set", your_set)

# DIFFERENCE:
print(
    my_set.difference(your_set)
)  # it is going to find the different of the first set with second set, any duplicate which in the set gets ignored, and its only show the differents.

print(your_set.difference(my_set))
# DISCARD
# my_set.discard(5)
# print(my_set)

# DIFFERENCE_UPDATE()
# my_set.difference_update(your_set)
# print("my_set", my_set)
# your_set.difference_update(my_set)
# print("your_set", your_set)

# INTERSECTION()
# print(
#     my_set.intersection(your_set)
# )  # It will return the common value from the both set
# OR INTERSECTION FOR THE OTHER HAND
# print(my_set & your_set)

# ISDISJOINT()
# print(my_set.isdisjoint(your_set))

# UNION()
# print(
#     my_set.union(your_set)
# )  # union just united the sets together but removed any duplicate, and its return the new set.
# OR SHORT HAND OF UNION
# print(my_set | your_set)


# ISSUBSET()
new_set = {4, 5}
print(new_set.issubset(your_set))

# issuperset()
print(new_set.issuperset(your_set))
