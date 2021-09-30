from time import sleep


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        print("Пожалуйста подождите...")
        for key, value in self.__color.items():
            sleep(value)
            print(key)


# Программа будет выводить цвета через определенные промежутки времени

traffic = TrafficLight(color={
    "Красный": 7,
    "Желтый": 2,
    "Зеленый": 3})
traffic.running()
