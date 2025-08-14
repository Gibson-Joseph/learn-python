# Exercise: Functions


# MY SOLUTION
def highest_even(li):
    all_even_num = []
    for item in li:
        isEven = item % 2 == 0
        if not isEven:
            continue
        all_even_num.append(item)

    higher_num = 0
    i = 0

    for i in all_even_num:
        if i > higher_num:
            higher_num = i

    return higher_num


print(highest_even([10, 2, 22, 98, 888, 3, 100, 5, 7, 25]))


# ZTM SOLUTION
def ztm_highest_even(li):
    evens = [i for i in li if i % 2 == 0]
    # evens = [i if i % 2 == 0 else "nothing" for i in li]
    return max(evens)


print(ztm_highest_even([10, 2, 22, 98, 888, 3, 100, 5, 7, 25, 999]))
