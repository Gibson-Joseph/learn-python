# CREATING OUR OWN OBJECTS


# Another rule is that usually you want it to be singular, not plural. Because it's blueprint
# We can create many characters, but those are going to be objects.
class PlayerCharacter:
    def __init__(self, name, age):
        # the __init__ is a special method. You can see the two underline here, this is called dunder or magic method
        # When we're building a class, you usually see this at the top.
        # This is what's often called a constructor method or an init method
        # This is automatcially called any time we instaniate
        # Instantiate means is we're calling class to create an object.

        # What is the "self" keyword
        # Self is a defalut parameter.
        # Here the default always the first parameter when we're defining a method is "self".
        # This is a way for us to define, Well, self refers to the PlayerCharacter.

        self.name = name  # These are attributes or properties that the instantiate variable have.
        self.age = age

        # What if without self?
        # AttributeError: 'PlayerCharacter' object has no attribute 'name'
        # first_name = name

    def run(self):
        print("run")
        return "done"


# player1 = PlayerCharacter()
# TypeError: PlayerCharacter.__init__() missing 1 required positional arguments: 'name'

player1 = PlayerCharacter("Cindy", 44)
# We can get the all method using DOT notation
# Note: "self" refers to whatever's to the left of the DOT. (player1.name)
print("player1", player1.name)

player2 = PlayerCharacter("Tom", 20)
print("player2", player2.name)

# Also we have access to run the method
# print(player1.run)
# <bound method PlayerCharacter.run of <__main__.PlayerCharacter object at 0x7655a41ff410>>

print(player1.run())

player2.attack = 50
print("player2.attack: ", player2.attack)
