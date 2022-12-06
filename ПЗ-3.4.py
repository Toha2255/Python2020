def my_func(x, y):
    try:
        x = int(x)
        y = int(y)
        result = 0
        i = -1
        c = x
        if y == -1:
            result = 1 / x
        elif y == 0 or y > 0:
            result = 'Ошибка. Введите целое отрицательное число. '
        while i > y:
            x = c * x
            result = 1 / x
            i -= 1
    except ValueError:
        return 'Внимание! Первое число должно быть целым положительным, второе- целым отрицательным.'

    return result


print(my_func((input('Введите положительное целое число: ')), (input('Введите отрицательно целое число: '))))
