from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# используем в качестве итерратора zip_longest, (None, '9А') оставил по условию задачи
iterator = zip_longest(tutors, klasses)
print(list(iterator))
