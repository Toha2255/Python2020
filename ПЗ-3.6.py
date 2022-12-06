def int_func(user_word):
    litle = user_word[0]
    big = chr(ord(litle) - ord('a') + ord('A'))
    answer = big + user_word[1:]
    return answer


source = input('Введите слова с маленькой буквы: ').split()
result = []
for user_word in source:
    result.append(int_func(user_word))
print(result)