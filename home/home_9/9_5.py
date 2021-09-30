class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка с помощю: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка с помощю: {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка с помощю: {self.title}")


stat = Stationery("Без всего")
pen = Pen("Карандаша")
pencil = Pencil("Ручки")
marker = Handle("Маркера")
office = [stat, pen, pencil, marker]

for i in office:
    i.draw()
