# MRO - Method Resolution Oder.
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077464#overview


# MRO or method resolution order is rule that python follows to determine whey you run a method which one to run when you have such complicated inheritance structure.

# ONE
# =======================
# class A:
#     # Class Object Attribute
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass


# print(D.num)  # 1
# # MRO is simply saying what's first in line if thigns are common bertween classes, methods or variables or atributes? what should I pick? And there's actually a good way for us to check this if we do the following;

# print(
#     D.mro()
# )  # [<class '__main__.D', <class '__main__.B', <class '__main__.C', <class '__main__.A', '<class 'object'>]
# # This is the order or the Mro of "D" class
# # It says, Hey, I'm going to check D first. If you call, D.num, I'm going to check __main__.D first, then I'm going to check __main__.B, then I'm going to check __main__.C and then I am going to check __main__.A and finally I am going to check the base class object. This is the order that it checks for "NUM".


# Two
# =======================
class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


# print(M.mro())
# or
print(M.__mro__)
# When I think
# [M, B, Y, Z, A, Z, Y, Z, object] #(It's wrong)

# Actually I got like the following in the log
# [M, B, A, X, Y, Z, object]

# Why this order, Well, the order is because of the way that we're passing in the parameters you see B is passed before A and Z , Why did X come before Z? Instead of going to what we would have thought would be Z, it goes to X, then Y, then Z, then the object. This is because of the algorithm that they use for doing Miro, which is called DEPTH FIRST SEARCH. As we can see, it's quite a bit confusing. And as a matter of fact, Python actually changed the MRO rules from what we have previousl in younger versions of Python. So this is another one of those things that got updated.

# MRO is there as way to define what order you're going to inherit it. And you can always use the MRO fucions or DUNDER to check this order.
