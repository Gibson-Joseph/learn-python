# Errors in Python

# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077570?start=15#overview
# https://docs.python.org/3/library/exceptions.html

# Unavoidable part of being a programmer is that your programs are going to give a lot of errors. You can't avoid bugs. You can't avoid programs breaking.

# print('Gibson) #SyntaxError
print(1 + "Gibson")  # TypeError

# An error, that crashes programs like above, its called an exception.
# Python, Raises these exceptions whenever the interpreter says, Hey, I have no idea what your doing, something's wrong. I don't know what I'm doing anymore, I'm going to stop whatever I'm doing and I'm going to give you an output.

# How can we handle these exceptions that crash our program? Well, We need something called ERROR HANDLING.

# The key takeaway is that the error handling allow us to let the Python script continue running, even if there are errors.

# Errors that are exists in python:
# 1. SyntaxError - Something is not a python standard.
# 2. NameError - Something is not defined
# 3. TypeError - trying to do something between two different data types that are incompatible.
# 4. IndexError - List index is out of range
# 5. KeyError - Something we trying to access a key that does not exists in dict.
# 6. ZeroDivisionErro - Division by Zero - 5/0
