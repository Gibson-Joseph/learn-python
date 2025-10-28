# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16126003#overview
import unittest
import script


class TestScript(unittest.TestCase):
    def test_input(self):
        result = script.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = script.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = script.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        with self.assertRaises(TypeError):
            script.run_guess("11", 5)


if __name__ == "__main__":
    unittest.main()
