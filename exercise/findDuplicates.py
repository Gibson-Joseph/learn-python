# Exercise: Check for duplicates in list:
# NOTE: You are not allowed to use Set
some_list = ["a", "b", "c", "d", "m", "n", "a", "n", "c", "c"]


print("MY SOLUTION")
original = []
duplicates = []

for item in some_list:
    (
        (duplicates.append(item) if item not in duplicates else None)
        if item in original
        else original.append(item)
    )
print("MY DUPLICATES: ", duplicates)


print("\nZTM SOLUTION")

ztm_duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in ztm_duplicates:
            ztm_duplicates.append(value)

print("ZTM DUPLICATES", ztm_duplicates)
