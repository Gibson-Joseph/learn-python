# DOC STRINGS


def test(a):
    # Doc string
    """
    Info: this function tests and prints param a
    """
    print(a)


test("hello")
# help(
#     test
# )  # help is a built-in function for python. its it help to find oiut what a function does.

# One other way to do this is to use what we call a magic method or a dunder method.
print(test.__doc__)

# These DOC STRING are really useful to add comments and definitions to your functions so that when other people on your team or coworkers come across your function that you created, they're able to underestand what it does right away without searching your python files or multiple files
