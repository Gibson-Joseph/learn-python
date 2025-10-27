# Writing Unit Test

import unittest
import main

# https://docs.python.org/3/library/unittest.html#assert-methods

# You really want to have tests that are easy to read so that other people understand your test. Because when it comes to testing, readability is really, really important. We don't care as much about not repeating ourselves and making our code efficient, nice and small.


class TestMain(unittest.TestCase):
    # Make sure all the test names re unique.
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


# Here you can see here how we went from a very simple function and we started catching these errors and started realizing how our function was too simplistic that if we received a wrong input.
# By testing and breaking things, I was able to improve this function.
# Now the do_stuff function works a lot better in production.
# It allows us to check for any mistakes.

# this is individual files that should only be run when we run our tests.

if __name__ == "__main__":
    # unittest.main simply says, Hey, just run all the tests over here.
    unittest.main()

# So this is a standard way that you would have your unit test done with the unit test module.
