list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []

# Оптимизированное решение:
for i in list:

    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            list_2.append(f'"{int(i):02}"')
        else:
            list_2.append(f'"{i[0]}{int(i[1:]):02}"')
    else:
        list_2.append(i)
print(list)
print(' '.join(list_2))

###############################################
# Не оптимизированное решение:
# list[1] = '05'
# list[8] = '+05'
#
# list.insert(1, '"')
# list.insert(3, '"')
# list.insert(5, '"')
# list.insert(7, '"')
# list.insert(12, '"')
# list.insert(14, '"')
#
# list[2] = list[1] + list[2] + list[3]
# list[6] = list[5] + list[6] + list[7]
# list[13] = list[12] + list[13] + list[14]
#
# list.pop(1)
# list.pop(2)
# list.pop(3)
# list.pop(4)
# list.pop(8)
# list.pop(9)
#
# print(' '.join(list))
