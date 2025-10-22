# Fibonacci Nummber using the list and generator


def fib(num):
    a = 0
    b = 1
    for _i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(20):
    print(x)


# def feb2(num):
#     a = 0
#     b = 1
#     result = []
#     for _ in range(num):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b

#     return result


# print(feb2(20))
