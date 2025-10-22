# Packages
import shopping

# A package is simply a folder, And we learned about module, which is python files. A package is a level up. A package is a folder containing modules.
# So you can have a package with multiple modules inside of them(folder). So the shopping_cart.py is a module but the shopping folder is package.

import shopping.shopping_cart

print(
    shopping
)  # <module 'shopping' (namespace) from ['/home/gibson/Documents/gibson/learning/learn-python/shopping']>

print(
    shopping.shopping_cart
)  # <module 'shopping' (namespace) from '/home/gibson/Documents/gibson/learning/learn-python/shopping/shopping_cart'>

print(shopping.shopping_cart.buy("Apple"))  # ['Apple']

# One of the rules of packages of Python packages is that on the root of this package, you have to have an __init__.py file.
# What is __init__.py?
# Well, becuase the interpreter is going to read this __init_.py file and say, Oh, this is a Python package.
# Packages have __init__.py file and we have different modules in them.
