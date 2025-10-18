# Pure Functions

# Let's say we give it a list containing 1,2, and 3. If we give this input into the function, what we would expect with a pure funcition is for something to happen to this input that every time results in the same thing.

# [1, 2, 3] ==> fn ==> [2, 4, 6]

# A Pure function has two rules:
# One - is that given the same input, it will always return the same output. That is, every time we give [1, 2, 3] to a function that we create, It should always return the same output
# [1, 2, 3] ==> fn ==> [2, 4, 6]
# If we run the above function millions of times with the SAME INPUT, it should result in the SAME OUTPUT.

# Second - the idea of a function should to produce any side effects.
# What are side effects?
# Side effects are things that a function does that afffects the outside world. For example, If I was to pring something inside of this function, it affects the outside world. Because I'm printing something onto a screen. The screen is outside world.
# For Example - If this function(fn) was touching a varible that lived outside of different scope, that's a side effect.


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


# Test one
print(multiply_by2([1, 2, 3]))  # [2, 4, 6]
print(
    multiply_by2([1, 2, 3])
)  # [2, 4, 6] --> 1. SAME INPUT AND SAME OUTPUT. 2. It doesn't produce any side effects(It doesn't touch outside the world(outside scope))

new_list = []


def multiply_by3(li):
    for item in li:
        # Here we have interacted with new_list variable from the outside of the multiply_py3 world. So this function has side effects.
        new_list.append(item * 3)
    return new_list


# new_list = "" #  So the new_list that lives in the outside world of the mylitply_by3 function can be modified by another developer or by a program.

print(multiply_by3([1, 2, 3]))  # [3, 6, 9]
print(multiply_by3([1, 2, 3]))  # [3, 6, 9, 3, 6, 9]--> SAME INPUT DIFFERENT OUTPUT


# When you have pure functions, you have less buggy code, you're able to test your code better, it's easier to understand your code and overall you have these benefits of not having different parts of your code touching each other and affecting each other, which makes our life as a programmer so much easier.


# IT IS IMPOSSIBLE TO HAVE PURE FUNCTIONS EVERYWHERE, because if a function doesn't affect the outside world at all, we wouldn't have any programs. Try to create pure functions and only have few non pure functions that maybe interact with the outside world.

# In functional programming, we don't need to combine data with functions, let's keep those separated. So we can foucs and pure functions and we can foucs on data.
