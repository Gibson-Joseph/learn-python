# Debuggin in Python:
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16112803?start=15#overview

# Ref: https://docs.python.org/3/library/pdb.html

# Linting
# Linting allow us to detect as we code some issue with our code.
# For example, if we do num + 4 here and we get a red underline any we see lint error
# num + 4
# Linter notice the error before we even rum our code.
# So Linting is allows us to find these errors before even run our code.

# PDB - Python Debugger
# ----------------------
# Ref : https://docs.python.org/3/library/pdb.html
# pdb is a built in module in python
# pdb is extremely useful because is allow us to interact with the code.

import pdb


def add(num1, num2):
    # Our code is tried to run, then it passed as soon as it said PDB set_trace. And then we can test it out what'g going on this function throught terminal.
    pdb.set_trace()
    print(num1, num2)
    t = 4 * 5
    return num1 + num2


add(2, "Gibbs")  # TypeError
# add(3, 1)

# inside the pdb in terminal commands;
# help
# list
# help list
# step - it's allow us to go to the next line.
# continue - it's continue and exit out of the PDB
# a - it will give the all the arguments of the current function that we are in.
# w
