# Filter

# with MAP function we always got the same number of items back.
# With FILTER function, we can somtime receive less then what we gave it. We're filtering some of the results.

# The filter function is going to try and receive a true and false value or a boolean value, whether it should be filtered or it should not.


def only_odd(item):
    return item % 2 != 0


print(
    filter(only_odd, [1, 2, 3, 4, 5])
)  # <filter object at 0x7f1cc91fef80> # We get filter object at this memory location(0x7f1cc91fef80).

# filter automatically give us this object(<filter object at 0x7f1cc91fef80>) that it has created in this memory(0x7f1cc91fef80)

print(list(filter(only_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
