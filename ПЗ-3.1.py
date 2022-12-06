def division(number_1, number_2):
    try:
        result = int(number_1) / int(number_2)
    except ValueError:
        return eror_2
    except ZeroDivisionError:
        return eror
    return result


eror_2 = 'Ошибка. Необходимо ввести целое число. '
eror = 'Ошибка. Делить на 0 запрещено. '
resultAnswer = division(input('Введите перевое целое число '), input('Введите второе целое число '))
print(f"Результат деления - {resultAnswer}")