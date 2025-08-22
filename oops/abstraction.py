# Abstraction in OOP (Hiding comples details and showing only the essential features)

# Abstraction means hiding of information or abstracting away information and giving access to only what's necessary.
# So whatever the user or the programmer or the macchine is interested in, that's only thing we give access to, everything else we kind of hide it in a blanket underneath the hood because our users don't have to worry about it.


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Run")

    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old")


player1 = PlayerCharacter("Gibson", 25)
player1.speak()

# Method
# Do we need to know how the count method was implemented? No. Because we don't really need to. If we try to understand every single little piece, our head is going to explode. Sometimes all we need is a method or an attribute and just get access to it without having to worry about how it's being implemented, which is really, really nice.
print((1, 2, 3, 3).count(3))

# Built-in function
# We get the length of 4, but we don't really need to know how length was implemented in Python, IT'S ABSTRACTED AWAY FROM US. And this is the power of OOP.
print(len([1, 2, 3, 4]))

# OOP abstracts away things that we don't need to care about, or at least it makes us more effcient so that we konw that it works a certain way and we're not wasting our time learning or coding from scratch.

# If we had our iPhone, for example, well, the camera feature on an iPhone, it'll be nice for an app that we build to use it, but we don't need to actually know exactly how the iPhone camera is coded on an iPhone. Instead, the iPHone usually gives us a way to say Camera.takePicture() to actually allow us to take a picture without knowing how the Apple engineers actually coded the camera. So it's a very powerful concept.

player1.name = "!!!!"
player1.speak = "Gibbsss Joseee"

# print(player1.speak())  # TypeError: 'str' object is not callable
# because of this error is speak has been modified. Speak  has been modified to a string value instead of this actual function that we could have needed.

print(player1.speak)  # Gibbsss Josee.
# I mean, abstraction is good, but hold on a second here. This is bad. If I have a class that've abstracted away, but anybody can come along, any programmer can come along and just remove all my hard work and overwrite it like above. Isn't that bad

### CONTINUE ON PRIVATE VS PUBLIC VARIABLE FILE
