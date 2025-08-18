# What is OOP? (Object oriented programming)

# Everything in python is an object.

print(type(None))  # <class 'NoneType'>
print(type(True))  # <class 'bool'>
print(type(5))  # <class 'int'>
print(type(5.5))  # <class 'float'>
print(type("Hi"))  # <class 'str'>
print(type([]))  # <class 'list'>
print(type(()))  # <class 'tuple'>
print(type({}))  # <class 'dict'>

# We can see that have all our data types, but we have this "class" keyword in front of it.
# Everything here is an object because in python, everything is built by this class keyword.
# And we're able to use different methods on our objects, to perform some actions on them.

# What is an object?
# Objects have methods like these and attributes that you can access with the DOT method
print("gibson".upper())

# Object oriented programming allows us to go beyond what python just gives us, which are these data types.
# The key takeway is that we're able to create our own types, our own data types with different attributes and methods.

# OOP is what we call a paradigm. It's a way for us to think about our code and structure our code in a way that is easier to maintain, extend and write.


################
# Our own class


# class or Blueprint of objects
# The blueprint class is going to be stored in memory.
# But everytime we create an object. We don't have to rewrite the code or do anything like this. We can simply say, Hey, go in memory to where big object is and just run that code so that again we're keeping our code DRY.
# We have one place that allows us to instantiate our code into objects.
class BigObjects:  # This is blueprpint for objects. But here we haven't actually created the object.
    pass


# instances (new object)
# Whare are the instances? These all are all objects.

# Creating a new objects
obj1 = (
    BigObjects()
)  # Here the double brackets is us instantiating the class and saying, Hey class, use whatever you have code inside the this class and instantiate it and create a new objects.
obj2 = BigObjects()

print(obj1)
print(type(obj1))  # <class '__main__.BigObjects'>
# As of now we can ignore the __main__.
