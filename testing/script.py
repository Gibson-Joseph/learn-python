# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16126003#overview
import random

answer = random.randint(1, 10)
while True:
    try:
        guess = int(input("Guess a number 1~10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("You are a genius!")
                break
        else:
            print("Hey bozo, I said 1~10")

    except ValueError:
        print("please enter a number")
        continue
