# Non Local Keyword
# What variable do i have access to?


def outer():
    x = "local"

    def inner():
        # "nonlocal" is actually a new keyword in "python3".
        # The nonlocal keyword is used to refer to this "parent scope". It is a way for us to say, Hey, I want to use a variable that is not a global but is outside of the scope of my function (innter function)
        nonlocal x  # I don't want to create new "x" varible. I want to jump up the scope to my parent scope.
        x = "nonlocal"
        print("innter: ", x)

    inner()
    print("outer: ", x)


outer()

# 1. Start with local
# 2. Parent scope?
# 3. Global scope?
# 4. bulit in python functions
# 5. Paramter is also part of the local scope
