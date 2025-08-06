# Our Fist GUI

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

arrow_down = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1],
]

diamond = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

heart = [
    [0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

print("\nMY OUTPUT")
for matrix in heart:
    line: str = ""
    for item in matrix:
        line = line + ("*" if item else " ")
    print(line)

print("\nZTM OUTPUT")
# 1. iterate over picture.
# 2. if 0 --> print ' '
# 3. if 1 --> print *
for image in picture:
    for i, pixel in enumerate(image):
        if pixel == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")  # Need a new line after every row

print("\nCHAT GPT")
for row in heart:
    print("".join("*" if pixel else " " for pixel in row))
