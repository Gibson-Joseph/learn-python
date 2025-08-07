# Function


# def is short form of define
def say_hello():  # We have created the say hello function, we've defined it, and now its living somewhere in memory on our machine. However, in order to use a function, we have to call it with the brackets.
    print("Hello world")


# The reason functions are so powerful is beause of the principle that we've talked about. The idea of DRI, which stands for DO NOT REPEAT YOURSELF. functions are really, really useful when you have things that you want to do over and over. For example, the print function, we've used it a lot.

say_hello()


heart = [
    [0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


def show_image():
    # Whatever is indented here, that's part of this function.
    # And the beauty is that this block stays a memory for us.
    for image in heart:
        for i, pixel in enumerate(image):
            if pixel == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


# Function allow us to keep our code dry.
# We don't repeat ourselves and reuse things that our machines can do over and over.
show_image()
show_image()


# We get the function show tree at this location.
print(show_image)  # <function show_image at 0x7eb0b7a8c7c0>
# 0x7eb0b7a8c7c0 # This is just the location in memory.
