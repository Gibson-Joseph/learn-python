# Developer fundamental V

# TEST YOUR ASSUMPTIONS
# Well, any time you learn something new, maybe something i'm teaching you or something other instructor or book or resource is teaching you. You want to test your understanding and your assumptions because you don't want to have any magic black box that things are happening that you don't understand.

# You want to know how things are working so you can explain it to people.


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return self


player1 = PlayerCharacter("Gibbs", 25)
print(
    player1.run()
)  # <__main__.PlayerCharacter object at 0x73f2cf1032f0> # this output refering to the player1 instance

# The idea is to test and test your self as well and your understanding and say, if my assumption is that self is referring to the object that we create, how can we test it?
