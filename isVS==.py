# is Vs ==
print(True == 1)
print("1" == 1)
print(100 == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# == the double equal check for equality of the value

print("--" * 20)

# print(True is 1)
print(True is True)  # True
# print("" is 1)
print("1" is "1")  # True
print(100 is 1)
print([] is 1)
print(10 is 10.0)
print(
    [] is []
)  # False  # every time i created the list its added in the memory in somewhare
