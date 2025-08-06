my_list = [1, 2, 3]


print("FOR LOOP")
for item in my_list:
    print(item)

    # When we use the BREAK statement, it breaks out of the current and closing loop, we just exited it.
    # break  # We can use BREAK in for loop as well

    # With a CONTINUE, what we're saying is, hey, whatever happens when you hit this line, CONTINUE on the top of the enclosing loop.
    continue
    print(item)


print("WHILE LOOP")
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    # When we use the BREAK statement, it BREAKS out of the current and closing loop, we just exited it.
    # break

    # With a CONTINUE, what we're saying is, hey, whatever happens when you hit this line, CONTINUE on the top of the enclosing loop.
    continue
    print(my_list[i])


# PASS is not very usefull. It essentially does nothing. It just essentially passes to the next line. So why is that ever useful?
# it's very rare that you'll see pass in your code, but pass is a good way to have, let's say, placeholder while you're coding.
for i, item in enumerate(my_list):
    # You want to loop through the for loop, but we don't know what we want to do yet in the code. Let's say that here we're still thinking about it.
    # So PASS is one of those placeholders that we can use so that there is a line of code that does absolutely nothing that we can still PASS through.
    # A very rare thing to see in production code, but while your're developing some developers like using pass.
    pass
