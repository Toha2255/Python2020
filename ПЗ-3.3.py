def my_func(number_1, number_2, number_3):
    number_min = min(number_1, number_2, number_3)
    if number_3 == number_min:
        summ = number_1 + number_2
    elif number_2 == number_min:
        summ = number_1 + number_3
    elif number_1 == number_min:
        summ = number_3 + number_2
    return summ


answer = my_func(int(input('Введите первое целое число: ')), int(input('Введите второе целое число: ')),
                 int(input('Введите третье целое число: ')))
print(f"Сумма наибольших цисел = {answer}")
