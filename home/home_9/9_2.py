class Road:
    def __init__(self, length, width, thickness):
        self.__length = length
        self.__width = width
        self.thickness = thickness

    def weight(self):
        all_mass = self.__length * self.__width * 25 * self.thickness
        print(f"{self.__width}m * {self.__length}m * 25.0 кг * {self.thickness} см= {all_mass / 1000} Т")


road = Road(length=float(input("Введите длину дороги в метрах: ")),
            width=float(input("Введите ширину дороги в метрах: ")),
            thickness=float(input("Введите толщину асфальта в сантиметрах: ")))
road.weight()
