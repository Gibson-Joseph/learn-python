# Why do we need scope?


# Questions:
# Why not just have everything as global varibles.
# How easy would it be if everything was just on the main page? All our information, all the data on our global scope so that everything has access to everything, wouldn't that be easier?


###
# But you have to remember that machine don't have infinite power, don't have infinite CPU, don't have infinite memory. They all have limited resources.
# And as programmers, we have to be conscious of what resources we use, because sometimes that can cost us money, sometimes they can crash our computers. And scope is a greate demonstration of this.


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("innter: ", x)

    inner()
    print("outer: ", x)


outer()
# For example, When this function is run, we're creating technically just one location in memory for the "x" variable. So we have that bookself in our computer that is "x" that's pointing to local when we actually call this. And when we say nonlocal, we are saying just don't create another bookself for us. Just use the one that we already have and assign it non-local.

# We learned that functions allow us to not repeat ourselves and being able to call out or multiple times. But another good use of function is that once we call this function and all of this is done, the computer and python interpreter specifically destroys all this memory. That's, once we finish with outer function, I can't really call print x outside of the function. Its going to give us an error. It's going to say, I have no idea what "x" is and why is that?
