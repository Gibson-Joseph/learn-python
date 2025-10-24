# Regular Expressions
# Ref: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16116101#overview
# Ref: https://www.w3schools.com/python/python_regex.asp

import re

# Regual expressions become really useful is for advanced patterns.
# You can think of regular expression as an entire language in itself with different patterns to use to find patterns inside of text.
# https://regex101.com/

# ([a-zA-Z]).([a])
# How are you!?

pattern = re.compile(r"([a-zA-Z]).([a])")
# 'r' stands for a RAW string

# ([a-zA-Z]): captures one alphabetic character (either uppercase or lowercase).
# .: matches any single character (except newline).
# ([a]): captures the letter “a” exactly.
# So this pattern matches a letter, followed by any character, followed by ‘a’.


print(pattern)

string = "search this inside of this text please! Gibosn!"
a = pattern.search(string)
print(a.group())  # sea
print(a.group(1))  # s
print(a.group(2))  # a

# https://regexone.com/
