import math


def generator():
    for el in fact:
        yield math.factorial(el)


fact = [5, 10, 4]
g = generator()
print(g)

for el in g:
    print(el)
