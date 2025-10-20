# Decorators
# Remember, a decorators supercharages our function. It's simply a function that wrap another function and enhances it or changes it.

# If something is a first-class citizen...
# It means you can:
# 1. Assign it to a variable
# 2. Pass it as an argument to a function
# 3. Return it from a function
# 4. Store it in a data structure (like a list or dictionary)


def my_decorator(func):
    def wrap_func():
        print("************")
        func()
        print("************")

    return wrap_func


# In Python, as soon as we write an @ in front of this is going to say, this is going to be a decorator and the decorator as loog as we follow this syntax my_decorator functoin of accepting a functon, having a wrapper function, calling the function and return the wrapper function can be used.


@my_decorator
def hello():
    print("Hellloooo")


hello()  # Hellloooo
print()
# We can do anything inside of our wrapper function.


@my_decorator
def bye():  # Here we've super booster our bye function
    print("See ya later!!")


bye()
print()


def hello2():
    print("Helllo 222222")


# Underneath the hood, all it does literally this
hello3 = my_decorator(
    hello2
)  # All I am doing is wrapping my hello2 function with my decorator and assigning it to variable. here the hello3 is equal to wrap_func
hello3()  # so here the wrap_func gets called.
# And the same as like bellow too
print()

my_decorator(hello2)()
print()

# Now the reason the decorators are useful is because instead of doing this (my_decorator(hello2)()) frankly looking confusing, I can just add at my decorator and we don't need to all of this (my_decorator(hello2)())


@my_decorator  # Now the hello4 function gets automatically wrapped by decorator
def hello4():
    print("Hello 44444")


hello4()
