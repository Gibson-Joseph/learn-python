# Built-in modules
# Python built-in modules: https://docs.python.org/3/py-modindex.html

# The beauty is, whenever we install Python on our machine, we get access to all built-in modules.

# NOTE: Run this file like $ python3 6_builtInModules.py gibson joseph

import sys

print(sys)  # <modul 'sys' (built-in)>
# sys is really, really useful one thay we are going to see a lot of.

# argv give us some interesting powers. Up till thi point, we've just kind of run our code inside our IDE.
print(sys.argv)  # ['6_builtInModules.py', 'gibson', 'joseph']
# here the first index actually the file name, and then you can get the optional names

first = sys.argv[1]
last = sys.argv[2]
print(f"Hii, {first} {last}")  # Hii gibson joseph
