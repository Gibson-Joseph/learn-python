# Inheritance in OOP


# Inheritance allows new objects to take on the properties of existing objects. So you can inherit classes.


class User:  # Parent class
    # Now, you might be wondering, where is the __init__ method here? Shouldn't we have that __init__ method that gets run first? Well, We could, but if we don't have any varibales or attributes that we want to assign to the user, well, in that case we wouldn't need and a __init__ method. So for now, we'll just say that we don't need there's nothing that the user other than this SIGN_IN method.
    def sign_in(self):
        print("logged in")


# Here, Ideally, all these Wizards and Archers are users as well.
# Here, All need to have the sign_in.


# How do we do inheritance? All we do is in the bracket, pass the parent class that we want to inherit from.
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


# wizard1 = Wizard()
# print("wizard1", wizard1)  # <__main__.Wizard object at 0x7e92...>
# print(wizard1.sign_in())  # logged in


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)

wizard1.attack()
archer1.attack()


# Using inheritance, We're keeping our code DRY. We're abstracting away the part of the User class code that they both share, but then changing things according to each one(Wizard class and Archer class) needs.

# For example, I could have different methods and properties on Wizard than Archer, but also have shared user's functionality that they have. And this way it keeps our code organized and clean.

# And the Key in inheritance is that we have a parent class and children class. Now, sometimes these children class are called subclass or derived class because they're subclasses or derived class, because they're subclasses User or derived from the user class.

### CONTINUE ON INHERITANCE PART 2#
