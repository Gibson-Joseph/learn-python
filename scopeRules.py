# SCOPE RULES
# What variable do i have access to?

a = 1


def confusion():
    # Here "a" is a local scope
    # a = 5  # Python interpreter going to creating a variable here called "a" in my own universe.
    return a


print(confusion())  # 5
print(a)  # 1


def parent():
    # 1. Start with local
    # 2. Parent scope?
    # 3. Global scope?
    # 4. bulit in python functions

    a = 10  # parent scope

    def confusion():
        # local scope
        return a
        # return sum

    return confusion()


print("parent scope: ", parent())

# There is a set of rules that the python interpreter goes through to check a variable.
# 1 - First its going to check with local
# local scope: A local scope is a scope that's part of the function
# 2 - If there's nothing in the local variable or local scope, is there a parent local scope?
# 3 - Global - Global is what we call the indentation of nothing. Whatever the file has, that is global.
# 4 - built in python or built in python functions
# python comes with predefined function such as sum().
