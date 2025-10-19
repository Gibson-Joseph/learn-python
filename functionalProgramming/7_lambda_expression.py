from functools import reduce

# Lambda Expression.
# Lambda is actually a computer science term that really is compatible with this idea of functional programming.
# Lambda expression in python are one time anonymous function that you don't need nore than once.

# Lambda expression is really, really useful when you're using them for function that "a" you only use once
# Lambda expression is anonymous function, that is becuase we only use them once, So we don't need to have a name for them because we don't need to store them anywhare on our machines.

# Lambda is looks like this:
# labmda param: action(param)

my_list = [1, 2, 3]

# Map
print(list(map(lambda item: item * 2, my_list)))
# Lambda expressions are one time anonymous functions, there is no name attachec to this funciton. And you don't need run more than once. So once the interpreter runs this line of code, it doesn't remember this function, it just forget about it, but its performs the action for us.

# And other language might not have lambdas, but they are sometimes called anonymous functions.

# Filter
print(list(filter(lambda item: item % 2 != 0, my_list)))


# Reduce
print(reduce(lambda acc, item: acc + item, my_list, 0))  # 6
