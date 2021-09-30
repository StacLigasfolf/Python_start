from random import choice


class Car:
    direction = ["🡡 north", "northeast 🡥", "east 🡢", "southeast 🡦",
                 "south 🡣", "🡧 southwest", "🡠 west", "🡤 northwest"]

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Полицейская машина? : {self.is_police}")

    def go(self):
        print("Автомобиль начал движение")

    def stop(self):
        print("Машина остановилась")

    def turn(self):
        print(f'Машина повернула {choice(self.direction)}.')

    def show_speed(self):
        print(f'Cкорость: {self.speed}.')


class TownCar(Car):
    def town_car(self):
        print(f"Городской автомобиль марки: {self.name}")

    def speed_control(self):
        print(f'{self.name}: Ваша скорость: {self.speed}. Притормозите!' if self.speed > 60 else super().show_speed())


class SportCar(Car):
    def sport_car(self):
        print(f"Спортивный автомобиль марки: {self.name}")


class WorkCar(Car):
    def work_car(self):
        print(f"Рабочий автомобиль марки: {self.name}")

    def speed_control(self):
        print(f'{self.name}: Ваша скорость: {self.speed}. Притормозите!' if self.speed > 40 else super().show_speed())


class PoliceCar(Car):
    def police_car(self):
        print(f"Автомобиль марки: {self.name}")

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


towncar = TownCar(90, "red", "Subaru", False)
towncar.town_car(), towncar.go(), towncar.show_speed(), towncar.speed_control(), towncar.turn()
print("*********************************************************")
sportcar = SportCar(150, "Green", "Lamborgini", False)
sportcar.sport_car(), sportcar.go(), sportcar.show_speed(), sportcar.turn()
print("*********************************************************")
workcar = WorkCar(75, "White", "Reno", False)
workcar.work_car(), workcar.go(), workcar.show_speed(), workcar.speed_control(), workcar.turn()
print("*********************************************************")
police = PoliceCar(90, "Black", "Ford", True)
police.police_car(), police.go(), police.show_speed(), police.turn()
