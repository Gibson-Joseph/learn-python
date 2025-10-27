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
# And that is when we do this, we actually get more information about the test that we ran So it gives you little bit more detail. You see which tests we're run and which once are okay, which ones have failed
# As a matter of fact, I can even add comments and doc string to my tests.


class TestMain(unittest.TestCase):
    # Make sure all the test names re unique.
    def test_do_stuff(self):
        """
        HIIIII!!!
        """
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


if __name__ == "__main__":
    unittest.main()

# Output:
# test_do_stuff (test_example_1.TestMain.test_do_stuff)
# HIIIII!!! ...Ok
# test_do_stuff2 (test_example_1.TestMain.test_do_stuff2) ... ok
