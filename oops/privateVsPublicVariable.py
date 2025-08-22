# Private Vs Public Variabales

# The idea behind abstraction is that we hide away infromation and only give access to things that user is concerned about.

# Some languages allow us to have private variales, for example, in a language like java.
# In python, there's no true privacy, no true private variables.


class PlayerCharacter:
    def __init__(self, name, age):
        # For private, what we would do is do underscore name or underscore age. Does this give any special power? Nope, this is just a convention that is as programmers, as python programmers, we deteremined that hey, If we see underscore in our code, that most likely means that this should be a private varible.

        # I am letting you know ahead of time if you see underscore, this shouldn't be modified, this should be private. And that's how we achive privacy in Python.

        # So If you ever want to keep a method or a an attribute private, you just put an underscore in front of it, BUT IT'S NO GUARANTEE.
        self._name = name
        self._age = age

        ## What about the double UNDERSCORE INIT (__init__)

        # This is dunder method, That is, it's built into python. And we usually never write our own Dunder Methods. We would never write double underscore. like following
        # self.__name = name
        # These double underscores and there's lots of them have special meaning in Python.
        # And the reason that they're named like this is because they're saying, hey, if you're writing double underscore for your varibale, you're doing something very wrong. You're aboute overwrite something.

        # So once again, this dobule underscore is also a convention to let people know you shouldn't really touch this or modify this with each data type.
        # So this idea of a private field is important to python. And although we can overwrite a lot of things, it's bad practice.

        # The idea is to abstract away this code, and although it can be modified and overwritten, by useing these proper conventions like PRIVATE ATTRIBUTES, we're able to abstract things away, but still make sure that whatever the user might be using isn't going to break our code.

    def run(self):
        print("Run")

    def speak(self):
        print(f"my name is {self._age}, and I am {self._name} years old")


player1 = PlayerCharacter("Gibson", 25)


player1._name = "!!!!"
player1.speak = "Gibbsss Joseee"
print(
    player1.speak
)  # Gibbsss joseee, that's because, like I said, no true private variables. As programmers, we've decided that underscore means that you shouldn't touch this. Please don't touch this.
# I am letting you know ahead of time if you see underscore, this shouldn't be modified, this should be private. And that's how we achive privacy in Python.
