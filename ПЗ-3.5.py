def programm(userList):
    try:
        q = 0
        while True:
            userList = list(input('Введите последовательность чисел (для выхода из программы нажмите "0"): ').split())
            myUserList = list(map(float, userList))
            for j in myUserList:
                q += j
            print(f'Сумма чисел = {q}')
            if j == 0:
                break
    except ValueError:
        print('Внимание! Последовательность должна быть представлена в виде цифр.')
    return q


programm(input('Здарвствуйте! Вы запустили программу по подсчету суммы последовательности чисел. Для продолжения нажмите "Enter".  '))
