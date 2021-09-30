for i in range(1, 101):

    if i % 10 == 1 and i % 100 != 11:
        print(f'{i} процент')

    elif 1 < i % 10 < 5 and not 11 < i % 100 < 15:
        print(f'{i} процента')

    else:
        print(f'{i} процентов')
