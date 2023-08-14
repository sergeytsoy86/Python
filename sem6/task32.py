# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

n = int(input('Введите количество элементов массива: '))
list = []
for i in range(n):
    list.append(random.randint(-10, 100))
print(list)

min_num = int(input('Введите минимальный элемент диапазона: '))
max_num = int(input('Введите максимальный элемент диапазона: '))
list_new=[]
for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        list_new.append(i)
print(list_new)


# строки 21-24 можно заменить (вариант решения без создания нового массива)

# for i in range(len(list)):
#     if min_num <= list[i] <= max_num:
#         print(i, end=' ')
# print('\n')