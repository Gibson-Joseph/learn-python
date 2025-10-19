# Map


# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list


# map actually allow us to simplify the code that we have here of multiply_by2


def multiply_by2(item):
    return item * 2


print(
    map(multiply_by2, [1, 2, 3])
)  # <map object at 0x7f1cc91fef80> # We get map object at this memory location(0x7f1cc91fef80).
# map automatically give us this object(<map object at 0x7f1cc91fef80>) that it has created in this memory(0x7f1cc91fef80)

# In order to view this object, we have to turn it into list like the following:
print(list(map(multiply_by2, [1, 2, 3])))
