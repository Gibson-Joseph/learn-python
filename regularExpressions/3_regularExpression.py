# Regular Expresssion


# Regual expression is a great thing to use for validation and just making sure that whatever a user inputs or whatever another machine inputs into your code is in the correct form.

# https://emailregex.com/index.html
# https://regex101.com/
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# The r before the string means it’s a raw string.
# The caret symbol (^) means start of the string.
# Square brackets [...] define a character set, meaning “match any one of these characters.”
# The at symbol must appear exactly as is — it separates the username from the domain.
# \. matches a literal dot (.).
# The dollar sign means end of the string.
# Parentheses create a capturing group, meaning this part of the pattern is captured (you can retrieve it later using group(1) or findall()).

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = "gibbs@yopmail.com"

a = pattern.search(string)
print(a)
