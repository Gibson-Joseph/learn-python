# Password Validations

# RULES:
# 1. At least 8 char long
# 2. Contain any sort letters, numbers, symbol such as $%#@
# 3. Has to end with a number
import re

pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")

password = "supersecret%$#8"

checkPass = pattern.fullmatch(password)
print(checkPass)

# [a-zA-Z0-9$%#@]
# The square brackets define a character class — it matches any one of the following characters:
# a-z → lowercase letters
# A-Z → uppercase letters
# 0-9 → digits
# $%#@ → any of these special characters ($, %, #, or @)
# {8,} → at least 8 characters long
# \d → a single digit (0–9)
