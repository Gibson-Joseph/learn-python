print(__name__)  # part of the #4
# Output: utility

# This utility MODULE holds, very simple functions, that we can all across our project.


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def sum():
    return "oops"


if __name__ == "__main__":  # This condition will only pass if we run this file
    print("Please run utility code")
