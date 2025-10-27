# Writing Unit Tests
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16126001#overview
# https://docs.python.org/3/library/unittest.html#assert-methods

import unittest
import main

# BY DEFAULT, UNITTEST ONLY DISCOVERS FILES NAMED:
# example: test*.py
# So make sure your file name starts with test_, for example:
# test_example.py
# Not like bellow:
# example_test.py
# example.py


# $ python3 -m unittest

# $ python3 -m unittest -v
# v stands for Verboase

# Tests are simply logical programs.

class TestMain(unittest.TestCase):
    # Another default method that we get with unit test is something called set up.
    def setUp(self):
        # setUp allows us to run a piece of code. Thats sets up before each call of the test.
        print("about to test a function")
        # This is really usefule, if you need to set up someting before each function. Let's say you have some default variables maybe that you need to setup. Well, in that case, this is a very useful method.

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "gibson"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def test_do_stuff4(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def test_do_stuff4(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def tearDown(self):
        # As the name suggests, we run it at the end of each method that we call.
        # Usually you do this to clean up some varibles, maybe reset some variables.
        # tearDown, we won't use as often. Usually we use it when are testing something more complicated like a database.
        print("cleaning up")


if __name__ == "__main__":
    unittest.main()

# Output with setUp:
# test_do_stuff (test_example_1.TestMain.test_do_stuff) ... ok
# test_do_stuff2 (test_example_1.TestMain.test_do_stuff2) ... ok
# test_do_stuff (test_example_3.TestMain.test_do_stuff) ... about to test a function
# Ok

# Output with setUp and tearDown:
# test_do_stuff (test_example_1.TestMain.test_do_stuff) ... ok
# test_do_stuff2 (test_example_1.TestMain.test_do_stuff2) ... ok
# test_do_stuff (test_example_1.TestMain.test_do_stuff) ... about to test a function
# cleaning up
# Ok
# test_do_stuff (test_example_2.TestMain.test_do_stuff2) ... about to test a function
# cleaning up
# Ok
