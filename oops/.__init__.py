# OOP constructor function
# .__init__


class PlayerCharacter:
    # Class Object Attribute
    membership = True  # Attribute

    def __init__(self, name="anonymous", age=0):  # constructor function
        # This __init__ function get called everytime we instantiate an new custome object
        # This __init__ function gives us a lot of control.
        if (
            age > 18
        ):  # We are able to add these safeguards to perhpaps make sure that we receive the right data type in order to create the object.
            self.name = name  # Attribute or Properties
            self.age = age

    def shout(self):  # Method
        print(f"my name is {self.name}")
        return "done"


player1 = PlayerCharacter("Tom", 10)

print(player1.shout())
