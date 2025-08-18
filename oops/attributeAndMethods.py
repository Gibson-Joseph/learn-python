# Attributes and Methods

# OOP allows us to write code that is repeatable, well organized and also memory efficient.


class PlayerCharacter:
    # Class Object Attribute.
    # The class object attribute, unlike these regular (self.name ro self.age) class attribute, is different because, well, it't NOT DYNAMIC. It's STATIC.
    # This is actuall attribute for PlayerCharacter class.
    # And this is something we use when there's no change. This is going to true and exist for all objects, so you can't really modify it. It's just all the objects that we instantiate will have access to it. So this is change accross instances.
    # We can use ths Class Object Attribute like the membership into the __init__ function or anywhere in this PlayerCharacter class  blueprint too.
    membership = True  # Attribute

    def __init__(self, name, age):
        # Attributes are pieces of data that are DYNAMIC. That is, when we instantiate an abject, they are going to be unique to that specific object like name and age.
        # And we had to use this "self" keyword to make sure that it was DYNAMIC.

        # if self.membership:
        # ( or )
        # This also works, becuse it's a CLASS OBJECT ATTRIBUTE.
        if PlayerCharacter.membership:
            self.name = name  # Attribute or Properties
            self.age = age

    # All methods receive the first parameter a self so that we can use them.
    def shout(self):  # Method
        print(f"my name is {self.name}")

        # print(f"my name is {PlayerCharacter.name}") # AttributeError: type object 'PlayerCharacter' has no attribute 'name'
        # Why this error? Because name is not a Class Object Attribute.

        return "done"


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 20)

# Using the new "help" function we actually get the entire blueprint of the object
# This "help" function is a great way to see what class blueprint some of the python data types have.
# help(player1)
# help(list)


# print(player1.membership)
# print(player2.membership)

print(player1.shout())
