# Generators
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077592#overview

# A very imporant key term and quite an advanced topic.
# Generators are available in Python and it allows us to generate a sequence of values over time.
# rage(100) is generator.

# A generator is a special type of thing in Python that allows us to use a special keyword called YIELD and it can pause and resume functions.

# range(100)
# list(range(100))


def make_list(num):
    result = []
    for i in range(
        num
    ):  # range is a generator. And a generator is a little bit different because this is not being held in memory when we do this for loop. This range doesn't create on its own a giant list of, lets say 0 to 99. And then it starts iterating.
        # for i in 0
        # for i in 1
        # for i in 2
        # for i in 3
        # ...
        # for i in 100
        # In memory, it never, ever creates this list like we have with my_list
        result.append(i * 2)
    return result  # this list lives in our memory


my_list = make_list(
    100
)  # my_list is pointing to a location in memory. So this is taking up space right now.
print(my_list)  # [0, 1, 2, ... 99]
print()

# Giant list
print(
    list(range(100000))
)  # That's a lot of memory that I'm using up. And once its done, only then can I use this list, and it's going to access that list in memory. And then we're able to use it a more efficent way is to use a generator and actually generate these 100 time without taking space in memory
