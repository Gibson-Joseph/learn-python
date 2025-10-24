# File path
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16125631?start=150#overview
# Ref: https://docs.python.org/3/library/pathlib.html
# The "with" statement in Python simplifies resource management by automatically handling setup and cleanup tasks.

# One of the common patterns when workng with files is to actually put them in try except block.
try:
    with open("app/happyone.txt", mode="r") as my_file:
        # text = my_file.write("I'am Happy to learn python")
        print(my_file.read())
except FileNotFoundError as err:
    print('file doesn"t exist', err)
    raise err
except IOError as err:
    # IOError usually happens when the computer or machine you're on has some issue reading or writing or doing any sort of IO operation.
    print("IO error", err)
    raise err

# this is a common way to work with files to handle different errors.
