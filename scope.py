# SCOPE

# scope is something present in a lot of programming languages

# Scope - what variables do I have access to?

# print(name())
# When we use something that it doesn't underestand or it doesn't have access to, it's going to throw a NAME ERROR or variable is not defined here.

# Scope in python has what we call functional scope or function scope.

# GLOBAL SCOPE
total = 100  # global scope, that means anybody on this file has access to this total variable.


# FUNCTION SCOPE
def sum_fun():  # You can think of this as a new universe.
    # think of scope as a new world that we create.
    # In our case, when we create a new function, we create a new world that anything that's indented inside of the function is its own world that we don't really have access to.
    sum_total = 100
    # We can only use total if we indent print()
    print(
        sum_total
    )  # This is part of the sum_fun world, that's what scope is. Who has access to who?


# sum_fun()

# print(
#     sum_total
# )  # sum_total is not defined, this is because of python's function scope.

if True:
    x = 10  # Althogh, we have indentation, the only time i create a new scope.

print(x)  # 10
