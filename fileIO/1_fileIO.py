# File I/O
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16125623#overview

# IO stantds for Input and Output.
# Most of the time machine are not communicating in just one environment.
# Maybe you want to speat to another website, maybe you want to speak to something that's on your desktop, maybe a file, maybe two different machines are communicating with each other, Mybe you speak to a database.

# IO simply means, Hey, I want you to input something from the outside world and output something into the outside the world.

# Reading and Writing files is very important.

# How can we do this file input and output in Python?
# Python has a built in function that allows us to open and write to files.


my_file = open("test.txt")  # Now we have the file object.

print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

# How can we read this file?
# print(my_file.read())  # Hii, My name is Gibbs Jose
# print(my_file.read())
# print(my_file.read())

# Here, I'm able to read the first around, but those two times(print) I'm not reading anything.
# Why is that?
# Well the open function has idea of a cursor. That is you can only read the file once. Once you open its return the file object, and the content of the file you can read. And the content of the file are red with cursor just like we see in the terminal one by one and printed on to the screen.
# But by the end of the first reading, the cursor is going to be at the end of the file.

# my_file.seek(0)
# print(my_file.read())  # Hii, My name is Gibbs Jose
# my_file.seek(0)
# print(my_file.read())  # Hii, My name is Gibbs Jose
# my_file.seek(0)
# print(my_file.read())  # Hii, My name is Gibbs Jose


# print(my_file.readline())  # Here we only get the first line.
# print(my_file.readline())  # second line
# print(my_file.readline())  # theird line

print(my_file.readlines())  # ['Hii, My name is Gibbs Jose\n', ':)\n', 'How are you?']
# Here we get the list that contains the entire file, raeds all the lines.

# BUT YOU ACTUALLY HAVE TO MANUALLY CLOSE THE FILE AFTER YOU'RE OPENED IT WITH OPEN FUNCTION.
my_file.close()  # You tell your computer, hey, you need to stop whatever you're doing. I am not interested in the file anymore, we're done with it.
