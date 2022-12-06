class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки!"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        if self.title == "Ручка":
            return "У вас ручка."
        else:
            return "У вас не ручка:)"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        if self.title == "Карандаш":
            return "У вас карандаш."
        else:
            return "У вас не карандаш:)"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        if self.title == "Маркер":
            return "У вас маркер."
        else:
            return "У вас не маркер:)"

q = Stationery('Title')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle(1)
print(q.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
