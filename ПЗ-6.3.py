class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def result(self):
        return f"Полное имя: {self.name + ' ' + self.surname} \nДоход: {self._income['wage'] + self._income['bonus']} rubls"


q = Position('Anton', 'Sidnev', 'Director', {'wage': 20000, 'bonus': 5000})
print(q.result())
