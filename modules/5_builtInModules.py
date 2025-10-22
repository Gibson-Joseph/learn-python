# Built-in modules
# Python built-in modules: https://docs.python.org/3/py-modindex.html

# The beauty is, whenever we install Python on our machine, we get access to all built-in modules.

import random

# Here we have do the alias, so in that case random become "noting". So you can actually avoid name collisions if we want.
import random as noting

print(
    random
)  # <module 'randam' from 'home/gibson/miniconda3/lib/python3.12/randon.py'>

# When we importing a library and we don't know what it does is to actually use the help function.
# help(random) # Now we can see the help messages.

print(dir(random))  # Its shows us all the methods available on this package.


print(random.random())  # it will give the random number between 0 and 1.
print(
    random.randint(1, 10)
)  # It will give the reandom nummber between start(1) and end(10) based on the arguments that we have passed to this function.

print(
    random.choice([1, 7, 42, 18])
)  # It will picks one value from the iterator list that we have provided.

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("my_list: ", my_list)  # It will shuffled our my_list in place.


print("noting: ", noting.random())
