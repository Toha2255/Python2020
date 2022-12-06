from functools import reduce

my = list((el for el in range(100, 1001) if el % 2 == 0))


def my_func(el, my):
    return el * my


print(reduce(my_func, my))
