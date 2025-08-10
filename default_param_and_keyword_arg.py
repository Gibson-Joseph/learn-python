# DEFAULT PARAMTER AND KEWORD PARAMETER


def say_hello(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


# positional arguments
# positional arguments are arguments that require to be in the proper position.
say_hello("joseph", "gibson")


# keword arguments:
say_hello(
    last_name="jose", first_name="gibbs"
)  # We tell it explictly, Hey I want last_name to this and first name to this.
# NOTE: Keyword arguemts are bad practice because we are making the code more complicated than it needs to be.


# Default parameter
def concat_string(first_name="Austin", last_name="Alwin"):
    print(f"Welcome {first_name} {last_name}")


# Keyword arguments can sometimes be confused with default parameters.
concat_string(first_name="Gibson", last_name="Joseph")
concat_string()  # With default paramets, it says if you are not able to get first_name and last_name because you are called without any arguments.
concat_string("Timmy")
concat_string(last_name="Timmy")
