# Useful modules

# datetime modules allows us to manipulate data values, which is really, really useful.

import datetime
from time import time

from array import array

# https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use


print(datetime.time())  # 00:00:00

print(datetime.time(8, 55, 2))  # 08:55:02 # So we can create a time object here.

print(datetime.date(2025, 12, 25))  # 2025-12-25

print(datetime.date.today())  # 2025-10-23

print(time())  # 1761233442.6454482


print("------------------------")

# This is little bit more performance than list. If you don't want to use generators, if you have a massive list, this is a quick, easy way to optimize your code.
arr = array("i", [1, 2, 3])
print(arr)  # array('i', [1, 2, 3])
print(arr[0])  # 1
