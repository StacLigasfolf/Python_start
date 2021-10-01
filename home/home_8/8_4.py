import os
import django
from collection import defaultdict


def dir_info():
    HomeWork = django.__path__[0]
    django_files = defaultdict(int)
    for root, dirs, files in os.walk(HomeWork):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            django_files[size] += 1

    for size, nums in sorted(django_files.item()):
        print(f'{size}: {nums}')


dir_info()
