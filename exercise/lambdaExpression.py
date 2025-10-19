# Exercise: Lambda Expression

# Square list:
my_list = [5, 4, 3]
print(list(map(lambda num: num**2, my_list)))

# List sorting based ont the second value
a = [(0, 2), (4, 3), (10, -1), (9, 9)]

# print(sorted(a, key=lambda item: item[1]))
# Or
a.sort(key=lambda item: item[1])
print("Sorted a is: ", a)
