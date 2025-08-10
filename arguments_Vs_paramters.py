# Aruguments Vs Parameters


# def say_hello():
#     print("Hello")


# The power of functions beyond just being able to call this multiple times because its only lives in one location in memory. Is this ability for us to make it dynamic?


# parameters
def say_hello(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


# arguments
# Arguments are used as the actual values  we proide to a function

# using arguments and paramters we made our function more extensible.
# We're keeping our code DRY and clean by doing someting like this.
say_hello("gibson", "joseph")
say_hello("joseph", "gibson")
