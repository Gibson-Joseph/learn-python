# Higher Order Functions (HOC)

# A higer order function can be one of two things. It could either be a function, let's say the greet function that accepts another function.


# Way - 1
# HOC
def greet(func):  # This is higher order function.
    func()


# It's a function that accepts inside of its parameters another function.

# Way - 2
# Another way it can be a higher order function is if it is a function that return another function.


def greet2():
    def func():
        return 5

    return func  # This is a higer order function


# A Higer Order Function is any function that either accepts a function as a paramter or return a function.

# Example HOC function;
# 1. map
# 2. filter
# 3. reduce

# Because its accepts a function.
