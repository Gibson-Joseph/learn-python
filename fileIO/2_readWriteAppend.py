# Read, Write, Append
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16125629#overview

# my_file = open("test.txt")
# print(my_file.readlines())  # ['Hii, My name is Gibbs Jose\n', ':)\n', 'How are you?']
# my_file.close()  # You tell your computer, hey, you need to stop whatever you're doing. I am not interested in the file anymore, we're done with it.

# Well a BETTER WAY to actually do something like the above and do fie IO with python is with the built in WITH STATEMENT.

# with open("test.txt", mode="r") as my_file:  # Here the my_file is a varible. defalut is read
# with open("test.txt", mode="w") as my_file:  # Now only write
# with open("test.txt", mode="r+") as my_file:  # Now read + write
# with open("test.txt", mode="a") as my_file:  # Now read + write
with open(
    "sad.txt", mode="w"
) as my_file:  # if the file doesn't exist it will create the the file or overwrite the existing one
    # text = my_file.write("Hey it's me!!")
    text = my_file.write(":(")
    print(text)  # 13
    # print(my_file.readlines())
    # Now "with open", you can actully do something like this, but you don't have to worry about closing.
    # this is the proper way to work with files in Python.

# What if we want to write a file?
# Underneath the hood open has a default paramter called MODE (more='r'), which stands for read. When we don't specify the mode it automatically just assumes we're reading.
# But if we want to write to a file. we can simply do 'w' for write.

# We want to be careful that we use the right mode based on what we need.
# The most common ones are read, write, append.
# We can creat any file like .py file If I wanted to.
