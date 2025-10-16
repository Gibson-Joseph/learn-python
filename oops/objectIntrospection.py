# Object introspection


# Introspection in computer programming means the ability to determine the type of an object at runtime.
# What is runtime? That is, when the code is running, you can determine the type of an object.
# It's actually one of Python's strengths, because everything in Python is an object we can examine.
# We can introspect and actually figure out what our code does as we're coding and then running.
# Python allows us to do introspection and inspect these objects with some nice helper functions.

# helper function - dir


class User(object):  # Parent class
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):  # Sub class
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


wizard1 = Wizard("Gibson", 42, "gibson@yavar.ai")

print(dir(wizard1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', ..., '__str__', '__subclasshook__', 'attack', 'name', 'power', 'sign_in']
# this dir finction give us all of the methods and attribute that the Wizard instat has.
# So with a dir function we give it an instance and right away we get access to what it has access to. We can see the name, power, sign_in.
# So this is really useful when you're trying to figure out what you have access to. We have a lot of these Dunder or magic methods that we haven't really talked about. What are these and why are they so important?

# Continue on Dunder Methods
