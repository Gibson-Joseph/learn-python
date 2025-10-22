# __name__
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16112769#overview

# As you start developing code, you're going to start to see a lot of code like beloow;
# if __name__ = '__main__':
# This is one of the most common line you are going to see when working with python.


from utility import divide, multiply
from shopping.more_shopping.more_shopping_cart import buy

print(buy("Orange"))
print(divide(2, 3))
print(multiply(2, 3))


# Output on the terminal:
# ----------------------
# utility
# shopping.more_shopping.more_shopping_cart
# ['Orange']
# 0.66666666666666
# 6

print(__name__)  # __main__
# Is the what you expected?

# maybe this (if __name__ = '__main__':) is starting to make sense now, when you see the code this (if __name__ = '__main__':) then do someting. And this __name__ "__main__" is given specifically to the file that we run.
# That one file that we run gets this default __main__.


# So the reason you might see line like bellow in Python is something we want to make sure that we run a module only if this is the main module.
if __name__ == "__main__":
    print("Please run this code")
