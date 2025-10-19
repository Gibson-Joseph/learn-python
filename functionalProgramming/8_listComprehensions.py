# List Comprehensions

# It's one of our key terms comprehensions.

# Well, they're actually called:
# 1. list comprehension.
# 2. set comprehension.
# 3. dictionary comprehension.

# And these are some of the data types that we have in Python.
# And we're able to use comprehension with these three data types.

# So what are these comprehension as well?
# They're a quick way for us to create lists or sets or dictionary in Python instead of perhaps looping or appending to bunch of items to lists.

my_list = []

for char in "Gibson":
    my_list.append(char)

# Here we have create a list that contains characters from "Gibson"
print(my_list)  # ['G', 'i', 'b', 's', 'o', 'n']

# Is there a faster, cleaner way of doing this?
# yes, there is with list comprehension in Python. You don't see it in a lot programming languages, but people that use Python really love this feature.

# The format we have follow like bellow;
# [param(expression) for param in iterable]

your_list = [char for char in "Joseph"]
print(your_list)

my_list2 = [num for num in range(100)]
print(my_list2)
print()

my_list3 = [num**2 for num in range(100) if num % 2 == 0]
print(my_list3)
print()

my_list4 = [num**2 if num % 2 == 0 else "XXXX" for num in range(100)]
print(my_list4)
