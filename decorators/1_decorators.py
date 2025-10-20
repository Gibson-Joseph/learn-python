# Decorators

# Decorator look like, they have the @ sign and then some sort of name following it.

# In Python function are what we call first class citizens. That is, they can be passed around like variables. They can be argument inside of a function. They act just like variables.


def hello():
    print("Hellllllooooooo")


# Remember, function are pretty much just variable Python.

# greet = hello()
# print(greet)

# greet = hello
# print(greet())

greet = hello
# A del keyword in Python that deletes that function
del hello

print(greet())  # Hellllllooooooo

# The interesting thing about Python is that We create hello function and this now created in memory. And we say, hey, greet is going variable to point to hello function.
# But when we do delete(del) hello function, all it does is say, hey, I'm going to delete this function, this name reference to this function that's in memory. However, because greet a whole another variable is still pointing to hello function. I am going to delete the helo function. So If I go hello function like the following;

# hello()  # NameError: name 'hello' is not defined.

# However the greet is still pointing in the memory to this location(hello).
# So Python is smart enough to say, Hey, you told me to delete hello, I'll delete the name hello. But I am not going to delete the function becuase greet is still pointing it(hello function).

# So functions in Python act just variable do


# We can also pass functions around inside the arguments
def hello1(func):
    func()


def greet1():
    print("Still here!")


a = hello1(greet1)

print(a)

# Decorators are only possible because of these features, this ability of function to act like variables, act like first class citizens in Python.
# Decorators supercharge our function
# By adding some sort of a decorator, we can supercharge our function and add extra functionaliy to it.

# decorator example

# @decorator
# def hello3():
#     pass

# It lets the python interpreter know I want this hello3 function have some extra feature.
