# Generators Performance:
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077600#overview

from time import time


def performance(fn):

    def wrapper(*args, **kwrags):
        t1 = time()
        result = fn(*args, **kwrags)
        t2 = time()
        print(f"took {t2-t1} s")
        return result

    return wrapper


@performance
def long_time():
    print("1")
    # A range, which is a generator that comes built into Python that is going to just one by one hold zero and memory and multiply by five, hold one memory, but multiply by five and keeps going, keeps going and removes from memory any old numbers.
    for i in range(100000000):
        i * 5


@performance
def long_time2():
    print("2")
    # This function uses a range and then converts it into list.
    # one create a list, and then from that list that's created in memory on our computers, it's going to go one by one and multiply things by five.
    for i in list(range(100000000)):
        i * 5


long_time()  # took 2.32 s, and this is so much faster even though they both do the same thing.
long_time2()  # took 3.90 s
# That's a pretty big difference.

# With generators, we're able to not hold things in memory, not have to consume all that resources and instead process data efficently.
# So generators are really, really usefull when calculating large sets of data, particularly if we're using long loops where we don't really want to store the memory, and we don't need to calculate everything at the same time, maybe one by one.

# And a lot of libraries in Python underneath the hood use generators instead using list because they're so much faster.


# To create a generator; All we have to do is create generator functoin that we want.
# def gen_fun(num):
#     for i in range(num):
#         yield i


# To use the generator function;
# for item in gen_fun(100):
#     pass
