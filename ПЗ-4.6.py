from itertools import count
from itertools import cycle

my_list = [True, 'Toha', 22, None]
i = 0
for el in count(5):
    if el > 1034:
        for q in cycle(my_list):
            if i > 5:
                break
            else:
                print(q)
            i += 1
        break
    else:
        print(el)

'''from itertools import count

for el in count(5):
    if el > 15:
        break
    else:
        print(el)

from itertools import cycle

i = 0
my_list = [True, 'Toha', 22, None]
for el in cycle(my_list):
    if i > 10:
        break
    else:
        print(el)
    i += 1'''
