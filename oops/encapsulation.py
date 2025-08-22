# Encapsulation

# ENCAPSULATION in Python programming (and in Object-Oriented Programming in general) refers to the bundling of data (variables) and methods (functions) that operate on that data into a single unit (class), while restricting direct access to some of the object’s components.

# In OOP the four things that object oriented programming does really, really well.

# What is encapsulation?
# Encapsulation is the binding of data and functions that manipulate that data.
# And we encapsulate into one big object so that we keep everyting in this box that users or code or other machines can interat with.
# And this data and functions are what we call attributes and methods.

# By using encapsulation, I've packaged all method and attribute up into a blueprint that we can create multiple objects.


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old")


player1 = PlayerCharacter("Gibson", 25)
player1.speak()

# Because of encapsulation, We have all this methods available to us, all these methods that we can access so that if I do, let's say capitalize, it will capitalize all our strings. We have all the methods like captialize, endswith, find, upper and etc.. for us to use
print("Gibson".capitalize())

# Why do we want to package data and functions into attributes and methods?
# Well, this gives us extra power.
