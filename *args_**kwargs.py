# ARGUMENTS AND KEYWARDS ARGUMENTS
# *args and **kwargs

# With the function actually have this special characters that we can use called args(*args) and star star keyword args (**kwargs)

# How can we use this?


# 1 *args:


def super_func(
    *args,
):  # This can accept any number of POSITIONAL ARGUMENTS like; super_func(1, 2, 3, 4, 5)
    # This way we can extend. And use our star args (*args) to have a function that can accept any number of arguments.

    print(*args)  # 1, 2, 3, 4, 5
    print(args)  # (1, 2, 3, 4, 5) will get args as tuple
    return sum(args)


total = super_func(1, 2, 3, 4, 5)
print("total", total)

# 2 **kwargs:


def add_num(*args, **kwargs):
    # *args -->> which is allow us to grab all positional arguments as tuple
    # **kwargs -->> which is allow us to grab all keyword argumetns as dict
    print("args", args)
    print(
        "kwargs", kwargs
    )  # Here we will get dictionary of default parameters like name and age
    total_value = 0
    for item in kwargs.values():
        total_value += item

    return sum(args) + total_value


print(add_num(1, 2, num1=3, num2=4, num3=5))


# Rule: params, *args, default parameters, **kwargs
def test(name, *args, age=25, **kwargs):
    print(f"name: {name}, age: {age}")
    total = 0
    for item in kwargs.values():
        print(item)
        total += item

    return sum(args) + total


print(test("gibson", 1, 2, 3, 4, num1=5, num2=6))
