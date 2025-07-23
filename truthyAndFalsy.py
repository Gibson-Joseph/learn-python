is_old = "Gibson"
is_licenced = 5

# is_old = bool("Gibson") #True
# is_licenced = bool(5) #True (This is what we call truthy and falsy value in python. Python do the type converstion on the vlaue)

print(bool("Gibson"))
print(bool(5))

if (
    is_old and is_licenced
):  # Actually this line check the truthy or the falsy value for the condtion statement like the following
    # if bool('Gibson') and bool(5)

    print("you are old enough to drive, and you have a licence!!")
else:
    print("You are not of age")
