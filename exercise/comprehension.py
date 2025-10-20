# Exercise: Comprehension
# Find the duplicate using the comprehension

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# My solution:
my_duplicates = list({char for char in some_list if some_list.count(char) > 1})
print(my_duplicates)
print()

# ZTM solution:
ztm_duplicates = list(set(x for x in some_list if some_list.count(x) > 1))
print(ztm_duplicates)
print()
