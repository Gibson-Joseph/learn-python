# Different ways to import modules
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16112767?start=15#overview

import shopping.more_shopping.more_shopping_cart  # This is getting little bit too cray. You can imagine as we have more and more packages that we constantly have to this import package.package.package.func

print(shopping.more_shopping.more_shopping_cart.buy("Apple"))

# How can we better this?
from shopping.more_shopping.more_shopping_cart import buy

from utility import divide, multiply

# from utility import *  # Instead of having multiple functions, you can do import with (*). It will import everyting from the utility module. But it always good to be explict and say exactly what you want to import.

print(buy("Orange"))
print(divide(2, 3))
print(multiply(2, 3))
# This is the really nice way to clean up our code.


# Another way to import modules:

from shopping.more_shopping import more_shopping_cart  # Import the entire module.

print(more_shopping_cart.buy("Mango"))

print(sum([1, 2, 3]))  # TypeError sum() takes 0 positional argument but 2 were given.
# This is error will occure if we use the (*) to import all function from the utility module. Because utility module has sum functoin that does'n accept the arguments. Here we have overwriten the Python's sum buit-in function.

# The key takeaway here is that modules and packages help us to have good engineering practices and build big projects in an organized fashion.
