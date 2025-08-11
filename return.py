# RETURN
# Return is a keyword in python. We are going ot see a lot when working with functions.


def sum(num1, num2):
    # function always have to return something, and when they don't return anything like there's no return keyword here, it automatically reutns none.
    # num1 + num2

    # If we add return, it's going to say as soon as we get to this line, I want you to exit this function.
    # When you exit this function, I want you to return whatever this expression gives us.
    return num1 + num2


print(sum(4, 5))

# A function either modifies something in our program or returns something.

# rules of function
# 1. Should do on thing really well.
# 2. Should return something.

total = sum(10, 5)
print(total)


def sumTwo(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func(num1, num2)


second_total = sumTwo(1, 2)
print(second_total)
