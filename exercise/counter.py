# COUNTER
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = None
for item in my_list:
    total = total + item if total else item

print(total)

