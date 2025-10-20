# Decorators Pattern


# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         func(*args, **kwargs)

#     return wrap_func


def my_decorator(
    func,
):  # Decorator pattern; Its give our decorator flexibility so that we're able to pass as many arguments as we want into our wrapped function by using args and kwrags thten unpacking them inside of a function.
    def wrap_func(*args, **kwargs):
        print("************")
        func(*args, **kwargs)  # Unpacking the args and kwrags
        print("************")
        print()

    return wrap_func


# What happens if the hello function took a paramter?
@my_decorator
def hello(greeting, emoji=":("):
    print(greeting, emoji)


hello("Hello Gibson joseph!!!", ":)")
hello(
    "Hello Gibson joseph!!!",
)
