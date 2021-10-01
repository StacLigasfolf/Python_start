def benchmark(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения программы : {end - start} секунд")
    return wrapper()

@benchmark
def prin():
    print(type(15 * 3))
    print(type(15 / 3))
    print(type(15 // 2))
    print(type(15 ** 2))
