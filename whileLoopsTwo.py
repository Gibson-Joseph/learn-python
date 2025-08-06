# While loop
my_list = [1, 2, 3, 4, 5]

print("FOR LOOP")
# For loops are simpler, like this code reads really nicely and really well. We just want loop over something that we already know how many times we want to loop over three times with times.
for item in my_list:
    print(item)


print("WHILE LOOP")
# Whild loops are very flexible, we can do a lot because we have this conditional statement. We can loop more than three times if we really wanted to. So in that case, wihle loops are more powerful but for loops are simpler.
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


print("WHILE WITH TRUE")
# While loops are extremely useful for tasks like this where looping can happen for a long time, you don't know how many times its going to happen, but this is something that you're just going to happend.
while True:
    response = input("say sometings: ")
    if response == "bye":
        break
