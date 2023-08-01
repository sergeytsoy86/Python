"""
Задача 2
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.
"""
# n = 123
# n1 = n // 100 # Нахождение первой цифры числа
# n2 = (n % 100) // 10 # Нахождение второй цифры числа
# n3 = n % 10 # Нахождение третьей цифры числа
# res = n1 + n2 + n3
# print(res)

"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
"""
# n = 6
# n1 = n // 6
# n2 = n // 6
# n3 = (n // 6) * 4
# print(n1, n3, n2)

"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
"""
# n = 385916
# n1 = n // 100000
# n2 = (n % 100000) // 10000
# n3 = (n % 10000) // 1000
# n4 = (n % 1000) // 100
# n5 = (n % 100) // 10
# n6 = n % 10
# if n1 + n2 + n3 == n4 + n5 + n6:
#     print('yes')
# else:
#     print('no')

"""
Задача 8: Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
"""
# a = 1
# b = 3
# c = 2

# if c <= b * a and (c % a == 0 or c % b == 0):
#     print('yes')
# else:
#     print('no')

'''Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
'''
#list_1 = [1, 2, 3, 4, 5]
#k = 3

# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)
'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
'''
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

# items = [1,2,3,4,5,16,7,12] # список чисел
# value = 10         # число к которому найти ближайшее
 
# def nearest_value(items, value):
#     '''Поиск ближайшего значения до value в списке items'''
#     found = items[0]        # принимаем допущение что ближайшее число к искомому первое в списке (с индексом 0)
#     for item in items:      # для каждого элемента (item) из items (т.е. попеременно item=1, item=2..)
#         # проверяем условие если разница между item value по модулю меньше разницы found и value, то
#         if abs(item - value) < abs(found - value): # если условие истинно (True)
#             found = item # меняем значение нашего допущения на item (т.е. item оказался ближе к искомому значению)
#     return found # возвращаем ближайшее значение до value в списке items
 
# print(f'Ближайшее число к {value} в списке {items} является {nearest_value(items, value)}')
# global_dict = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'C': 1, 'Т': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#                'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'D': 2, 'G': 2,
#                'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'B': 3, 'C': 3, 'M': 3, 'P': 3,
#                'Й': 4, 'Ы': 4, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#                'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'K': 5,
#                'Ш': 6, 'Э': 6, 'Ю': 6, 'J': 6, 'X': 6,
#                'Ф': 7, 'Щ': 7, 'Ъ': 7, 'Q': 7, 'Z': 7}

# string = input(k).upper()
# result = 0
# for item in string:
#     result += global_dict[item]
# print(result)

# 2 вариант решения задачи

points = {"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т": 1,
"DGД, К, Л, М, П, У": 2,
"B, C, M, PБ, Г, Ё, Ь, Я": 3,
"F, H, V, W, YЙ, Ы": 4,
"K ЖЗХЦЧ": 5,
"JXШЭЮ": 8,
"QZФЩЪ": 10}
# .lower() <-> .upper()
word = input("Введите текст: ").upper()
count = 0
# "Ivan"
# 0123
for char in word:
    for key in points:
        if char in key:
            count += points[key]
print(count)