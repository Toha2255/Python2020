class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f'Скорость автомобиля = {self.speed}'

    def go(self):
        return 'Автомобиль в пути. '

    def stop(self):
        return 'Автомобиль не едет. '

    def turn_right(self):
        return 'Автомобиль повернул направо. '

    def turn_left(self):
        return 'Автомобиль повернул налево. '


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Скорость превышена! "
        else:
            return f'Скорость автомобиля = {self.speed}'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Скорость превышена! "
        else:
            return f'Скорость автомобиля = {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - это пиолицейская машина!'
        else:
            return f'{self.name} - это гражданский автомобиль.'


dodge = SportCar(100, 'Apple', 'Dodge Demon', True)
toyota = TownCar(30, 'White', 'Toyota', False)
kamaz = WorkCar(70, 'Orange', 'Kamaz', False)
ford = PoliceCar(110, 'Black', 'Ford', True)
print(dodge.show_speed())
print(toyota.show_speed())
print(ford.police())
print(kamaz.turn_left())
