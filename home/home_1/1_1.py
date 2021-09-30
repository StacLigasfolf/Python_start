# пользователь задает секунды
duration = int(input("Введите секунды: "))
time = ['hour', 'min', 'sec', 'day']
# Расчет времени от секунд до часов
time[2] = duration % (24 * 3600)
time[0] = time[2] // 3600
time[2] %= 3600
time[1] = time[2] // 60
time[2] %= 60
# * Добавляем дни, 86400 - это кличество секунд в дне
if duration >= 86400:
    time[3] = duration // 86400
# Ввывод на экран
print(f"{time[3]} дн {time[0]} час {time[1]} мин {time[2]} сек")
