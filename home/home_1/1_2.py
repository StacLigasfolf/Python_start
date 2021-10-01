# Задаем списки, контеинеры
list_cudes = []
add_cubes = []
sum_cubes = 0
# Задаем кубы нечетных чисел и добавляем их в список
for i in range(1, 1000):
    cub = i ** 3
    if cub % 2 == 1:
        list_cudes.append(cub)
# Ищем числа сумма цифр которых нацело делится на 7
for index, numb in enumerate(list_cudes):
    summ = 0
    while numb > 0:
        summ += numb % 10
        numb //= 10
    if summ % 7 == 0:
        sum_cubes += list_cudes[index]
    # Добавляем 17 к каждому элементу списка
    list_cudes[index] += 17

print(sum_cubes)
# Теперь выводим значение уже с добавлением 17
sum_cubes = 0
for index, numb in enumerate(list_cudes):
    summ = 0
    while numb > 0:
        summ += numb % 10
        numb //= 10
    if summ % 7 == 0:
        sum_cubes += list_cudes[index]

print(sum_cubes)
