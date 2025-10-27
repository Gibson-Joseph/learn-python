# Testing in Python

# As the name suggests, testing is a method in software development where individual units of source code, such as function, are tested to see whether they work propery.

# A test is simply another Python file.
# Each one of the modules will have its own test file that you can run tests with.
# This test file that we're going to be writing never actually runs in production. It's a file that we run to make sure that before we release our main file tor production, that everything is working properly. So this is only for development.

# VS Code extenstions:
# =====================
# 1. Pylint extenstion - that we installed in our Visual Studio code to link our code and check the syntax and small errors as we type our code
# 2. Pyflakes is a another linter
# 3. AutoPEP 8 extension - which is the standard style guide for Python. And this allows to make sure that our code meets a style that Python community has agreed on.

# These are the simple tools that allow our code to be checked for simple styling issues or simple mistake, such as not declaring a variable.


# there is built in module from the standard library that we can use, And its called unittest.
import unittest
