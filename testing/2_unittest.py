# Unittest

import unittest
import main

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

# We want to import our test file after we import our unittest.


# The unit test works is we create a class and then name it whatever you want.
# And we inherit inside of this class what unit test gives us, which is a TestCase.
# This is just standard way to work with unit test.


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        # In here we can test our code.
        test_param = 10
        result = main.do_stuff(test_param)
        # This last line is a key part of unit test.

        # The assertEqual is someting that we get when we inherit from unittest.
        self.assertEqual(result, 15)
        # self.assertEqual(result, 13)

    def test_do_stuff2(self):
        test_param = "gibson"
        result = main.do_stuff(test_param)
        # https://docs.python.org/3/library/unittest.html#assert-methods
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)
        # What we're trying to do with our tests is to imporove our function by simply trying to break it.


# Now finally we just run the unit test.
unittest.main()
# This will run the entire test file with in the TestMain class


# Output
# ======
# Ran 1 test in 0.000s
# Ok

# Or
# AssertionError: 15 != 13
