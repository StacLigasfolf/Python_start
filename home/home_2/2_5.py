marekt = [57.3, 21.2, 45.32, 34.82, 68.32, 52.4, 18.3, 93.17, 43.23, 66, 9, 21, 45.32, 34.32, 68.12, 52.4, 18.7,
          93.12, 10.2]

# Задание А - вывесли цены в виде: "5 руб 04 коп"
for i in marekt:
    r, kop = str(f'{i:.02f}').split(".")
    print(f'{r} руб {kop} коп')

# Задание B - сортировка по возрастанию без нового list[]
# доказываю с помощю id, что обьект списка остался тот-же
print(f'before: {id(marekt)} - {marekt}')
marekt.sort()
print(f'after: {id(marekt)} - {marekt}')

# Задание C - создать новый список, содержащий те же цены, но отсортированные по убыванию.
list = sorted(marekt, reverse=True)
print(f"descending list: {list}")

# Задание D - вывести цены пяти самых дорогих товаров.
print(f' 5 самых дорогих товаров: {list[:5][::-1]}')
