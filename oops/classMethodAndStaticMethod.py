# @lassmethod and @staticmethod


class PlayerCharacter:
    # Class Object Attribute
    membership = True  # Actually attribute for PlayerCharacter class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # With this decorator, we can write a function
    # classmethod aren't used as often.
    # We use something like a class method when we do care about these dynamic attribute and maybe we want to modify them or change them.
    @classmethod  # decorator
    def adding_things(cls, num1, num2):
        # cls stands for class. This pointing the PlayerCharacter class
        # Why do we need this? We can use the cls to actually instantiate an object in here
        # return num1 + num2
        return cls(
            "Teddy", num1 + num2
        )  # <__main__.PlayerCharacter object at 7f9906ec4f98>

    # The staticmethod works the exact same way like the classmethod. Except you do not have access to the cls or class, So  we can't do something like we did in the classmethod.
    # So we would use something like static method where we don't care anything about the calss state. A class state is something like dynamic attribute, we don't care about the attributes really.
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

    # So the only difference between the @classmethod and @staticmethod is the idea that we don't have access in our paramerts to this cls.
    # These classmethod and staticmethod is something that we  won't see very often.

    def shout(self):
        print(f"my name is {self.name}")


# player1 = PlayerCharacter("Tom", 20)
# print(player1.adding_things(2, 3))

# This is a method on the actual class.
# print(PlayerCharacter.adding_things(2, 4))  # 6

player3 = PlayerCharacter.adding_things(
    2, 4
)  # We can create a whole new player here that was created by using this classmethod method.
print(player3.age)
