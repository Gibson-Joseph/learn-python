# Error Handling:

# So, we've just created a program that isn't going to error out, hopefully, at least with ValueErros and ZeroDivisionError. But sometimes errors and exceptions can be so severe that we do want to stop our program from running.
# We do want to catch them like this with the except block, but at the same time also stop whatever the program is doing.
# Well, in that case, we either DON'T USE THE EXCEPT BLOCK or in here we can say RAISE.
while True:
    try:
        age = int(input("What is your age? "))
        10 / age
        # This is rare that you would have to do this. There are some specific use cases, but here you would just write a message like bellow.
        # So here, we are able to throw our own errors. So this is really useful if you're creating your own livrary or tool and your want to let the user know that and error happend. And this could be any type of errors.
        # raise ValueError("Hey cut it out")  # ValueError: Hey cut it out
        raise Exception("Hey cut it out")  # Execption: Hey cut it out
        # The key thing to remember with errors is that errors are unavoidable in programming. What our job is as a programmer is to be able to anticipate these errors, these bugs, these exceptions, and handle them properly in our programs.
        # There is no such things as a perfect program.

    # except ValueError as err:
    #     print(err)
    #     print("Please enter a number")
    #     continue
    except ZeroDivisionError:
        print("Please enter age higer than 0")
        break
    else:
        print("Thank You!")
        break
    finally:
        print("Ok, I am finally done!")
    print("Can you hear me?")
