# Guessing Game
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16112779#overview

# This is my soultion

# import random
# from sys import argv

# start = int(argv[1])
# end = int(argv[2])

# random_num = random.randint(start, end)

# while True:
#     try:
#         num = int(input(f"guess the random number between {start} to {end} : "))
#         if num == random_num:
#             print("You find that number!!")
#             break

#     except ValueError:
#         print("Please enter a number only")

# --------------------------------------------------

# This is ZTM solution
# 1. Generate number 1 to 10
# 2. Input from user?
# 3. Check the input is 1 to 10?
# 4. Check the number is right guess. Otherwise ask again

import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])

answer = randint(start, end)
print(answer)
while True:
    try:
        guess = input(f"guess the number {start} to {end} :   ")
        # if (value := int(guess)) > 1 and value < 11:
        if start < (value := int(guess)) < end:
            if value == answer:
                print("You're a genius!")
                break
        else:
            print(f"Hey Gibbs, I said {start} to {end}")
    except ValueError:
        print("Please enter a number")
        continue

# -----------------------------------

# https://pypi.org/
# Ref:https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16112783#overview
