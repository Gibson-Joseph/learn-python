# Modules In Python

# Modules are simply called files, well each one of the .py file.

# The way we commnunicate between those file is quite simple. All we need to do is use the import command we import and them give it the file name that we want to

import utility

print(
    utility
)  # < module 'utility' from '/home/gibson/Documents/gibson/learning/learn-python/modules/utility.py'>

# Now there's a few things that happend here.
# One is that we generate this __pycache__ folder. This __pycache__ is created every time we run a file with IMPORT STATEMENT, so when we're using modules.
# What __pycache__ does is when we run this file, the interpreter is going to create this __pycache__ folder. So see the file name inside the __pycache__ is .pyc, this is becuase it's using the C Python interpreter. So this is a actually a compiled file. This __pycache__ is just something that editors allow us to do just so our programs can run faster.

print(utility.multiply(1, 3))  # 4
print(utility.divide(1, 3))  # 0.33
# Now we can able to use the utility function in our my 1_module.py file.
