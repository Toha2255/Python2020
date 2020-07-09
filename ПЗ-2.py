time = int(input('Введите время в секундах '))
time_minuts = (time // 60) % 60
time_hours = (time // 3600) % 24
time_sec = time % 60
if time_hours < 10:
    time_hours = '0' + str(time_hours)
if time_minuts < 10:
    time_minuts = '0' + str(time_minuts)
if time_sec < 10:
    time_sec = '0' + str(time_sec)
print(f"Время  в формате: чч:мм:сс: {time_hours}:{time_minuts}:{time_sec}")
