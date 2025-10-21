# Error handling:


while True:
    try:
        age = int(input("What is your age?"))
        10 / age

    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("Please enter age higer than 0")
        break  # We can break out of the loop
    else:  # its will caled if there is no exception.
        print("Thank You!")
        break
    finally:
        # finally runs at the end after everything has beed executed.
        # finally says, Hey, no matter what, at the end of it all, I want you to finally do something.
        # So finally runs regarless at the end of everything.
        print("Ok, I am finally done!")
    print(
        "Can you hear me?"
    )  # this print statement will work if we don't have the break statement in the else block and finally
