# Reduce

from functools import reduce

# Reduce doesn't come as part of the python built in function. In order for us to use reduce, we have to do something like above. (from functools import reduce).


my_list = [1, 2, 3]


# this accumulator takes takes two parameters, And this is going to be called by reduce. So reduce going to be charge of giving these two parameters from the data we give it, which is my_list
def accumulator(acc, value):
    # the acc is going to default to ZERO if we don't give it anything in the theird argument of the reduce function
    return acc + value


# 1. We need the FUNCTION
# 2. We need the SEQUENCE or the DATA
# 3. We need the INITIAL VALUE

print(reduce(accumulator, my_list))  # 6
print(reduce(accumulator, my_list, 0))  # 6
# Actually we redced our list into some sort of data that we've manipulated.
