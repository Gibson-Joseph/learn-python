# Useful Modules

# We have some specialized data types that come as well built into the Python standard library.

from collections import Counter, defaultdict, OrderedDict

# Now notice how some of them are classes because they're capital letters, ans some of them(defaultdict) look to be just a function
# Counter

li = [1, 2, 3, 4, 5, 6, 7]
print(Counter(li))  # ({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1})
# It's create a dictionary

print(Counter([*li, 7]))  # ({ 7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
# It create a dictionary that keeps track of how many times an item occured in an iterable. Here the 7 occured twice.

sentence = "blah blah blah thinking about python"
print(
    Counter(sentence)
)  # ({'h': 5, ' ': 5, 'b': 4, 'a': 4, 'l': 3, 't': 3, 'n': 3, 'i': 2, 'k': 1, 'g': 1, 'u': 1, 'p': 1, 'y': 1})
# Here I see which letter occured the mose.

print("-------------------------")

# defaultdict
dictionary = {"a": 1, "b": 2}
print(dictionary["a"])
# print(dictionary["c"])  # KeyError: c

# Using the defaultdict we're actually going to get a default value if someting doesn't exist.
# here the first value should the callable object, and the callable means someting like a function that can be called so if we do run.
# dictionary1 = defaultdict(int, {"a": 1, "b": 2})
# print(int())  # 0
# print(dictionary1["c"])  # 0

# dictionary1 = defaultdict(lambda: 5, {"a": 1, "b": 2})
# print(dictionary1["c"])  # 5

dictionary1 = defaultdict(lambda: "Does not exists", {"a": 1, "b": 2})
print(dictionary1["c"])  # Does not exists
print(dictionary1["a"])  # 1

print("--------------------------")

# OrderedDict
# Order dictionary retains the order that you insert into a dictionary.

d = OrderedDict()
# d = {}  # Dictionary in Python has no sense of order.
d["a"] = 1
d["b"] = 2

d2 = OrderedDict()
# d2 = {}
d2["b"] = 2
d2["a"] = 1

print(
    d2 == d
)  # True if the order is same for both dict; This is going to check for the value

# https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/
