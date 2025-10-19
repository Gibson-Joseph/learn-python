# Zip

# The zip functon works kind of like a zipper.
# We need two lists or two iterables and we can zip them together.

my_list = [1, 2, 3, 4, 5, 6, 7]
# your_list = [10, 20, 30, 40]
your_list = (10, 20, 30, 40)
my_name = "Gibson Joseph"

print(zip(my_list, your_list))
print(list(zip(my_list, your_list)))  # [(1, 10), (2, 20), (3, 30), (4, 40)]

# Here zip takes two itratable and grabs the first item from each and zips them together like a zipper, So 1 and 10 get added to a tuple together and so on.

print(
    list(zip(my_list, my_name))
)  # [(1, G), (2, i), (3, b), (4, s), (5, o), (6, o), (7, '')]

print(
    list(zip(my_list, my_name, your_list))
)  # [(1, G, 10), (2, i, 20), (3, b, 30), (4, s, 40)]

# it's actually very important function that, because it's so generic, can be used in so many different things.

# For example: If we had from a database, we collected all the usernames from one column in a database and then maybe from another part of database we collect all of the phone numbers and they were all in the same order. Well we can combine these into tuple using zip that has username and phone number attached to them and create a whole new data structure.
