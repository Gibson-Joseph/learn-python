# Error handling
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077578#overview


def sum(num1, num2):
    try:
        # return num1 + num2
        return num1 / num2

    # By just doing except with no exceptions, as a programmer, we are reading this and we don't really know what actually went wrong, because it could be so many things. So a good practice is to always catch these erros based on a specific exception.
    # except:
    # except TypeError:

    # method - 1
    # Now a common pattern when doing error handling is to do someting like this type ERROR AS and then doing someting like the variable. So whatever variable we want in our case, let's just say ERR.
    # Here we are saying, Hey, if you catch type error, let us use error in our error message so we can say like bellow
    # except TypeError as err:  # err is a variable
    #     # here the err is the built-in error object. It's build in exception in Python.
    #     # print("Please enter numbers " + err)

    #     # print(err) # can only concatenate str (not "int") to str
    #     # It is very, very useful if we want to give meaningfull errors to our users.
    #     print(
    #         f"Please enter numbers: {err}"
    #     )  # Please enter numbers: can only concatenate str (not "int") to str

    # method - 2
    # Another interesting thing you can do is someting like below, where you wrap these errors together.
    # except (TypeError, ZeroDivisionError):
    #     # So we can handle multiple errors the say way.
    #     print("ooops!!")

    except (TypeError, ZeroDivisionError) as err:
        # So we can handle multiple errors the say way.
        print(f"ooops!! {err}")


# print(sum(1, 2))
print(sum(1, "2"))
