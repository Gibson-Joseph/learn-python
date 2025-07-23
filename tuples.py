# Tuples
# ======

# Tuples are like list but unlike a list we can't modify them. They are immuatable, you can think about them as immutable list
# Once you created it, it's the way it is

my_tuple = (1, 2, 500, 4, 5, 4, 1, 4)
print(my_tuple)
print(my_tuple[3])  # Just like a list you can access its with index
print(500 in my_tuple)

# Why do we need this??
# =====================
# 1. If you don't need to change the list, that make things easier, because its tell the other programer looking your code, Hey this should not be changed, I want like a list and i want this to stay the way it is.

user = {"basket": [1, 2, 3], "greet": "Hey Gibbs!!", "age": 24}
print(user.items())  # This will return the key:value as tuple

new_tuple = my_tuple[1:4]
print(new_tuple)

# =====================
x, y, z, *others = (100, 200, 300, 400, 500)
print("x", x)
print("y", y)
print("z", z)
print("others", others)

# =====================
print("Tuple count", my_tuple.count(4))
print(
    "Tuple index position", my_tuple.index(500)
)  # this will return the first index of the value that we have provided
print("Lenght of the tuple", len(my_tuple))

###### In simple tearm tuples are list but its not mutable
# =====================
