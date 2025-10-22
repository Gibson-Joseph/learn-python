# Generators:
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077596#overview

# print(
#     list(range(100000))
# )  # This massive list finally finished being entered in memory.

# Generators are actually iterable. That is everything that is a GENERATOR IS ITERABLE, you can iterate over them, but NOT EVERYTHING THAT IS ITERABLE IS A GENERATOR.

# For example;
# RANGE is generator, so that is always going to be INTERABLE.
# But the LIST is an iterable, but it's not a GENERATOR.
# So a generator is a subset of an iterable.

# The difference between a generator and a regular iterable is the way we implement them.


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


# General way to create a generator:
# Generators are usally functions just like range is a function.


# This is the standard way in Python that we can create a generator function using the RANGE and the YIELD keyword.
# This yield keyword gives us some power because if we just RETURN here, we're not going to get anything special. As a matter of fact, we're just going to ge a value.
# Instead by using the yield keyword, what we're able to do is to TURN THIS INTO A GENERATOR FUNCTION.
def generator_fun(num):
    for i in range(num):
        # instead of return like we would in a regual function, we're going to use a keyword called yield
        # you can notice the different betweent the MAKE_LIST and GENERATOR_FUN function
        # yield i
        yield i * 2
        # return i * 2
        # What does yield do? Yield paused the function and comes back to it when we do someting to it, which is called NEXT.
        # Yield says, Hey, pause the function, just yield i give i and when you tell me to keep going again, then I'll keep going.


# We are going to print each item in the generator_fun function, because this is an iterable. It's going to run and it's going to loop. And for every item in this number(range = 1000) so that it's range, we're goint yield "i" so it's going to keep looping and looping, when we comeback, when we loop over we're going to run this and the yield, comes back and runs again.
# for item in generator_fun(1000):
#     print(item)
# What we just did here is similar to make_list, but instead of having to create that list in memory, it just kept goint one by one. We only held one item in memory. And we used it however we wanted to. In our case, all we did was print item.

g = generator_fun(100)
# g = generator_fun(1)
print(g)  # <generator object generator_fun at 0x7f7dbe8a4c0>
# Here we get a GENERATOR OBJECT.
print(next(g))  # 0
print(next(g))  # 2
print(next(g))  # 4
# Why is that?
# Remember the yield keyword pauses the funciton.
# So what just happend generator_fun is we ran the function with 100. The first item in range 100 was 0

# YIELD PAUSES THE FUNCTION AND COMES BACT TO IT WHEN NEXT IS CALLED.
# So if function has a yield keyword, it becomes a generator. It keeps track the value, and it only keep the most recent data in memory for example "4" and its remember that

print(next(g))  # 6
