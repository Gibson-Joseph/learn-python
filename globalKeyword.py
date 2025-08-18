# GLOBAL KEYWORD
# What variable do i have access to?

a = 10


def confusion(b):
    # 'b', the parameter is part of the local scope, that is, its part of the confusion function. So parameter are considered local variables. We can use it inside the funcion not outside of this function.
    print("b is: ", b)


confusion(3)

total = 0


# def count():
#     total += 1
#     return total


# print(
#     count()
# )  # UnboundLocalError: cannot access local variable 'total' where it is not associated with a value.

# ======================================


# def count():
#     total = 0
#     total += 1
#     return total


# print(
#     count()
# )  # UnboundLocalError: cannot access local variable 'total' where it is not associated with a value.

# What if i wanted to run count function multiple time?
# count()
# count()
# print(
#     count()
# )  # here we still get '1', because every time we run the function, we reset the total with '0'.

# ======================================

###  When you attempt to assign a new value to a variable within a function, Python, by default, treats that variable as a new local variable within the function's scope, even if a global variable with the same name exists.

# def count():
#     # the global keyword says use the global 'total' if it exists so that instead of having to create a new variable, We can use the global varible 'total'

#     # However, this is actually not a good way of doing things, because it can get really confusing when you start adding global and all these different universe are accessing each other's variables.

#     # A better a way of doing this someting called DEPENDENCY INJECTION and this is a simplified version of it. The idea is that instead of accession variables outside of the function like 'global total', which, really complicated as files get bigger and bigger, is to do istead.
#     global total
#     total += 1
#     return total


# count()
# count()
# print(count())  # 3

# ======================================


# DEPENDENCY INJECTION
def count(total):
    # A better a way of doing this someting called DEPENDENCY INJECTION and this is a simplified version of it. The idea is that instead of accession variables outside of the function like 'global total', which, really complicated as files get bigger and bigger, is to do istead.
    total += 1
    return total


# count(total)
# count(total)
# its still '1'. because by the time we pint the third total, well, the 'total' varibale never changes. total varible is a global '0'
# print(count(total))  # 1

# If I run this
print(count(count(count(total))))  # 4 # this is completely insane. it looks confusing.


# ======================================
# 1. Start with local
# 2. Parent scope?
# 3. Global scope?
# 4. bulit in python functions
# 5. Paramter is also part of the local scope
