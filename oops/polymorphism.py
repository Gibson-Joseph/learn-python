# Polymorphism

# poly - means many
# morphism - means form.
# Many Forms

# We know that methods belog to objects. right? We use the self keyword to act upon the object that got instantiated.

# In Python, this idea of polymorphism refers to that way in which object classes CAN SHARE THE SAME METHOD NAME. But those method names can act differently based on what object calls them.


class User:  # Parent class
    def sign_in(self):
        print("logged in")

    def attack(self):
        # Its going to override whatever the original attack we have already have that mehtod in our Wizard class and Archer class.
        print("Do nothing")


class Wizard(User):  # Children class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # But let's say I wanted to have both User and Wizard class run the attack method. How can we do this?
        # Because We accept User as my parameter in here.
        # And also not have to repeat ourselves in case we want to use something like attack from User class inside
        User.attack(self)  # 'Do nothing'
        print(f"attacking with power of {self.power}")
        # So Polymorphism allows us to have many forms. It is the ability to redefine methods for these derived class that is Wizard and Archer


class Archer(User):  # Children class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 30)


# def player_attack(char):
#     char.attack()


# Here we can see that the same function gives me a different output, even though we're calling the same function, because of the objecct that we pass into it, Polymorphism.
# player_attack(wizard1)
# player_attack(archer1)


# for char in [wizard1, archer1]:
#     # Once again, we have two different outputs, even though i'm calling the same method because of the different objects. This is a really powerful concept.
#     char.attack()

print(wizard1.attack())
# And an object that gets instantated can behave in different forms id different ways based on Polymorphism.
# And this useful because we are able to modify our class to our specific needs.
