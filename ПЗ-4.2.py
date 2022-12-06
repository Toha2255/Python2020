my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([el2 for el1, el2 in zip(my_list, my_list[1:]) if el2 > el1])
