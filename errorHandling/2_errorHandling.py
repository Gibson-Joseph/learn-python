# Error handling

# Error handling allows us to let the script continue running, even if there is an error.

# try:
#     age = int(input("What is your age? "))
#     print(age)
# except:
#     print("Please enter a number")

# here, we have handling our errors by wrapping all of our code iny a try block, And what's going to happen is instead of our program erroring out before our program crashes, It's going to run this code and then it's going to say, Hey, If within the try block, anything happens, we'll catch it in except block.

# while True:
#     try:
#         age = int(input("What is your age?"))
#     except:
#         print("Please enter a number")
#     else:
#         print("Thank You!")
#         break

# We can simply give it what type of error we want to handle in except block.
# Built-in-errors
# https://docs.python.org/3/library/exceptions.html
while True:
    try:
        age = int(input("What is your age?"))
        10 / age

    except ValueError:
        # This except block ony accepts ValueError, any other errors it does not care about.
        # This except block going to run only once. As soon as catches the error its looking for, its going to run the except block, And then come back to the while loop.
        # So only one of the errors wiill be caught.
        print("Please enter a number")
    except ValueError:
        # This except block ony accepts ValueError, any other errors it does not care about.
        print("!!!")
    except ZeroDivisionError:
        # This except block ony accepts ZeroDivisionError, any other errors it does not care about.
        print("Please enter age higer than 0")
    else:  # its will caled if there is no exception.
        print("Thank You!")
        break
