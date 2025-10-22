# Under The Hood Of Generators
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077602?start=15#overview


# FOR LOOP
# This is how the FOR LOOPS really work underneath the hood.
def special_for(iterable):
    # This ITER function is going to use the NEXT function on this iterable
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)  # <list_iterator object at 0x7efcddd49e10>
            # In the log we can see that ITERATOR object existss in the same memory space, even though we're constant looping through 1 to 5
            # So this is how for loop work underneath the hood.

            # Here we can loop through some interable abojects useing next
            # next(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3, 4, 5])
# special_for(["1", "Gibson", True, [], None])


# What about the ranges?


# RANGE
# This is how the RANGE really work underneath the hood.
class MyGen:
    # And We are using a class here because remember we're just creating our own data type, our own special range in Python.

    # Class Object Attribute.
    current = 0

    def __init__(
        self, first, last
    ):  # This is how a range we're able to say, start with this and end with this.
        self.first = first
        self.last = last

    # We can use our dunder methods. We have define dunder that is ITER and ITER allows us to create an interable.
    def __iter__(self):  # This is built into Python
        return self

    def __next__(self):  # Because that's how next function works underneath the hood.
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 20)
for i in gen:
    # Here the for loop automatically catches the StopIteration error us, so it doesn't error out and it stop looping at the end
    print(i)  # 0 ... 19
