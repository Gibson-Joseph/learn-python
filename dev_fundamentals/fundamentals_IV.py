# FUNDAMENTALS

# clean
# Readability
# predictability
# DRY

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


# 1. iterate over picture.
# 2. if 0 --> print ' '
# 3. if 1 --> print *

# for image in picture:
#     for i, pixel in enumerate(image):
#         if pixel == 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")  # Need a new line after every row


fill = "|"  # instead of me having to change five locations here, i can now change just this part.
empty = " "  # Only had to change in one location
for image in picture:
    for i, pixel in enumerate(image):
        if pixel:
            print(fill, end="")
            # print(fill, end="")
            # print(fill, end="")
        else:
            # print(empty, end="")
            print(empty, end="")
    print("")  # Need a new line after every row
