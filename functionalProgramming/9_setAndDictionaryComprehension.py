# Set and Dictionary comprehension.

# Set comprehension:
# A quick way to generate sets.
# Sets only allow value that are not duplicate only unique items.
my_list = {char for char in "Gibson"}
print(my_list)
print()

my_list2 = {num for num in range(100)}
print(my_list2)
print()

# Dictionary comprehension:
simple_dict = {"a": 1, "b": 2}

my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)
print()

my_dict2 = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict2)
print()

my_dict3 = {
    key: value**2 if value % 2 == 0 else "XXX" for key, value in simple_dict.items()
}
print(my_dict3)
print()
# This makes our code litte bit less redable, so it's just a shorthand for us to use.

my_dict4 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict4)
print()
