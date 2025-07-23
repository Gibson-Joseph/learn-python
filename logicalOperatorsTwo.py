# LOGICAL OPERATORS (<, >, ==, <=, >=, !=, not) PART #2

is_megician = True
is_expert = False

# check if megican AND expert: 'You are a master megician'
if is_megician and is_expert:
    print("You are a master megician")

# check if megician but not expert: 'at least you're getting there'
elif is_megician or is_expert:
    print("At least you'are getting there")

# check if you're not a megician: 'you need a magic powers'
elif not is_megician:
    print("You need a magic power")
True