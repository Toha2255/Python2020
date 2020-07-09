plus = int(input('Выручка фирмы '))
minus = int(input('Расходы фирмы '))
if plus > minus:
    print("Фирма работает в плюс. Рентабельность фирмы: {:.2f}".format(plus / minus))
    workers = int(input())
    print("Прибыль фирмы в расчете на одного сотрудника: {:.2f}".format(plus / workers))
elif plus < minus:
    print('Фирма работает в убыток. ')
