def dict(name, last_name, birth, city, mail, tel_number):
    print(f"Имя - {name}; Фимилия - {last_name}; Год рождения - {birth}; Город проживания - {city}; e-mail - {mail}; Телефон - {tel_number}")


dict(name=input('Введите имя '), last_name=input('Введите фамилию '), birth=input('Введите год рождения '),
     city=input('Введите город проживания '), mail=input('Введите e-mail '),
     tel_number=input('Введите номер телефона '))
