# Dunder Method
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077458#overview


# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', ..., '__str__', '__subclasshook__']
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {"name": "Gibbs Jose", "has_pets": False}

    # Modify the __str__
    def __str__(self):
        # print(f"{self.color}")
        return self.color

    def __len__(self):
        return 5

    def __del__(self):
        print("deleted")

    def __call__(self):
        return "Yess??"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 0)

# Before modify the __str__ dunder function
print(action_figure.__str__())  # <__main__.Toy object at 0x7f4aa65be208>
# it's the exact same thing as us doing str(action_figure) like this.
print(str(action_figure))  # <__main__.Toy object at 0x7f4aa65be208>

# These double underscrore dunder methods are special methods that Python recognizes.
# For example, the DUNDER STR (__str__()), this special method allows us to use action_figure like this (str(action_figure)) using the str built in function.

# After the modifiy the __str__ dunder function
print(action_figure.__str__())
print(str(action_figure))  # red


# Just like dictionaries, lists, tuples, and all our objects in Python can behave in certain ways. How lists were accessed with an index number and a dictionary was access with key.
# list = [0]
# dictionary = 'key'
# Those are all implemented using these DUNDER method.


# After:
print(action_figure.__len__())  # 5
print(len(action_figure))  # 5

print(len("gibson joseph"))  # 13

# del
# del action_figure  # deleted

# Call
print(action_figure())

# Usually we don't want to overwrite them , but you just want know that you have the power to do so if you choose.

# Get Item
print(
    action_figure["name"]
)  # Gibbs Jose # Gibbs jose was being able to access using this bracket notation using the get item.
print(action_figure["has_pets"])  # Gibbs Jose

# So these special magic methods are really interesting because it allows us to do some custom modifying of our classes. And we can also understand how in Python are built in default types had access and abilities to have all these special syntax.
