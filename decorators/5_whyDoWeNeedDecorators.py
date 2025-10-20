# Why Do We Need Decorators?
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
    for i in range(100000000):
        i * 5


long_time()

# Decorators are used a lot in Python libraries and frameworks.

# Mybe you want to have some authentication decorator, so you do authenticate it where each function can only run if the user is authenticated, maybe they have the privilege to run a function such as logging in to a website.

# @auth
# def admin():
#     pass
