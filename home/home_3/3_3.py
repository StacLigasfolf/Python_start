from random import choice

words_1 = ["автомобиль", "лес", "огонь", "город", "дом"]
words_2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
words_3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes():
    """
    P/s знаю что сделал тапорно но ничего больше не приходило в голову, но условие задачи я выполнил :)
    Функция дял герерации шуток
    :param n: количество шуток
    :param слов в шутке ровно 3 (по условию)
    """

    n = int(input("Введите количество шуток: "))
    i = 1
    while i <= n:
        list_j = [choice(words_1), choice(words_2), choice(words_3)]
        print(*list_j)
        i += 1


get_jokes()
