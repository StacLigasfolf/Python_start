def benchmark(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения программы : {end - start} секунд")

    return wrapper()


@benchmark
def dict():
    user = str(input("Напишите число на английском: "))
    numbers = {
        "zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
        "seven": "семь",
        "eight": "восемь", "nine": "девять", "ten": "десять"
    }
    print(numbers[user])
