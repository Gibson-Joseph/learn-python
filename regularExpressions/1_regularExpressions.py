# Regular Expressions

# Regular expressions are not unique to python. As a matter of fact, you see them all over programming languages.

# Python comes with a regual expression module.
import re

# Regular exressions are very useful for finding things in a piece of text.

# string = "search inside of this this text please!"
string = "search this inside of this this text please!"

# This is a simple way for us to search someting inside of a string.
print("search" in string)  # True

# Then why do we need regual expressions?

print(re.search("this", string))  # <re.Match object; span(17, 21) match='this'>
# A regular expression gives us an output, not just true of false, but an actual object that tells us a little bit more information about the 'this'(string).
# We can see one of the information is the span. So where it occurs in the string, it occurs at index of 17 and ends at index of 21

a = re.search("this", string)
# What can we do with match object?

print(a.span())  # (17, 21)
# It tells us where the string occurs as a tuple.

print(a.start())  # 17
print(a.end())  # 21

print(a.group())  # this
# Group returns the part the string where there was the match.
# Group is really useful when we're trying to do multiple searches.

print("----------------------\n")

string2 = "search this inside of this text please!!"
b = re.search("THis", string)  # None
# If the regular function doesn't goint to find anything it's going to return none. So it's either goint to return a match object or none.
# print("b ==>", b) # None
# print(b.start())  # AttributeError

# print("----------------------\n")

# Another way is compile
string3 = "search this inside of this text please!!"
pattern = re.compile("this")
c = pattern.search(string3)
print(c.group())

d = pattern.findall(string3)
print(d)
# ['this', 'this'] # So we can get the both instances of 'this' inside of a list.

e = pattern.fullmatch(string3)
print(e)  # None; because we don't get a full match


text = "search this inside of this text"

pattern2 = re.compile("search this inside of this text")
f = pattern2.fullmatch("search this inside of this text")
print("f==>", f)
print(f.group())  # search this inside of this text

g = pattern2.match((text + "Gibson Joseph"))
# matches the string then doesn't care what comes afterwards.
print("g==>", g)
