# SET
# Sets are simply unorder collections of unique objects

# In a set there is no duplicate everything has to be unique
my_set = {1, 2, 3, 4, 5, 5, 1, 3}
print(my_set)

# Add
my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1, 2, 2, 3, 3, 4, 3, 5]
print(set(my_list))

print(10 in my_set)
print("Length of my_set is: ", len(my_set))

# CONVERT THE SET INTO THE LIST
print(list(my_set))

new_set = my_set.copy()
print("new_set is: ", new_set)
