class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):
    def get_full_name(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname} ")

    def get_total_income(self):
        print(f"Зарплата включая премию составляет {sum(self._income.values())} руб.")


position = Position("Иван", "Пупкин", "Менеджер", 25000, 5000)
position.get_full_name()
position.get_total_income()
