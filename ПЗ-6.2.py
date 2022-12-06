class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass(self):
        print(f"{(self._lenght * self._width * 25 * 5) / 1000} тонн")


r = Road(int(input('Введите длину: ')), int(input('Введите ширину: ')))
r.mass()
