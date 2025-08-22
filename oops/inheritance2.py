# Inheritance in OOP


# Inheritance allows new objects to take on the properties of existing objects. So you can inherit classes.

# So we have these class. Now the Python gives us a useful tool to check if soemthing is an instance of a class.


class User:  # Parent class
    def sign_in(self):
        print("logged in")


class Wizard(User):  # Children class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):  # Children class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")


# isinstance is a built in function in Python. We give it the instance and then the class that we want to check.
# isinstance(instance, Class)

wizard1 = Wizard("Merlin", 50)
print(isinstance(wizard1, Wizard))  # True # Wizard1 is an instance of Wizard Class.
print(isinstance(wizard1, Archer))  # False

print(isinstance(wizard1, User))  # True
# True # Because Wizard Class is a subclass of User class.
# So technically, yes, Wizard1 is an instance of User because we've had to run User class to create wizard1 instance.

# If we do the wizard1 dot (wizard1.), Do we see how I have our methods and attributes that we've added, but also all these Dunder Methods. Where do these come from? IN PYTHON EVERYTHING IS AN OBJECT. Everything in python inherits from the base OBJECT CLASS that Python comes with, and it's called OBJECT.

print(isinstance(wizard1, object))  # True
# It's True because wizard1 one inheritance or gets methods from the Wizard Class, from the User Class, and even HIGER UP from the OBJECT based class that Python comes with. And that's why we have these automatic methods attached for us.

# print([].)
# print(wizard1.)
# And this way we avoiding repeating code. And common functionality, we can dish it out to all the objects that need it, which is very, very cool.


# So underneath the hood, when we do something like User class, it's actually accepting OBJECTS as the parent class in ordet to accept these properties that are build in and that we might need in the future.
# e.g ==> class User(object):
