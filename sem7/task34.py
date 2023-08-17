# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

#1 вариант решения (через цикл for)

poem = input('Винни Пух напиши стих: ').lower().split() # <class 'list'> ввожу текст, перевожу все в нижний 
                                                        # регистр, разделяю на элементы списка пробелом 
rifma = list()                                          # создаю пустой список для проверки на рифму
for i in poem:                                          # циклом по элементам списка 
    count = 0                                           # счетчик количества 'a'
    for j in i:                                         # циклом по элементу списка (проверка букв - j)
        if j == 'а':                                     
            count += 1
    rifma.append(count)                                 # [4, 4, 4] заполняю список rifma результатами count                            
if len(set(rifma)) == 1:                                # <class 'int'> rifma преобразую в множество set(), и у 
                                                        # и узнаю количество элементов множенства len()
    print('Парам пам-пам')                              # если len(set(rifma)) == 1:, то в множестве 1 уникальный элемент
else:
    print('Пам парам')                                  # если len(set(rifma)) != 1, то множестве несколько элементов
                                                        # рифмы нет 

#2 вариант решения через функцию

def f(poem):                                          # функция f принимает poem(text) - можно называть по разному
    return sum(1 for i in poem if i in 'а')           # возвращает сумму повторов (1) буквы 'a' в poem(text)
    
text = input('Винни Пух напиши стих: ').lower().split()    

t = f(text[0])                                        # <class 'int'> в переменную t записала результат вызова f для индекса 0
                                             
if all([f(i) == t for i in text]):                    # функция all для всех вызовов фукнции f, если все True
    print('Парам пам-пам')
else:
    print('Пам парам')


#3 вариант решения (через lambda)


text = input('Винни Пух напиши стих: ').lower().split()# ввожу текст, перевожу все в нижний регистр,
                                                       # разделяю на элементы списка пробелом <class 'list'>
f = lambda x: sum(1 for i in x if i in 'а')            # x-элементы списка, i-элементы (элемента)-буквы, 1-счетчик sum
                                                       # lambda возвращет (return) количество повторов 'a' <class 'int'>
t = f(text[0])

if all([f(i) == t for i in text]):
    print('Парам пам-пам')
else:
    print('Пам парам')


#4 вариант решения задачи универсальный (со всеми гласными)

stroka = 'пара-ра-рам рам-пaм-папам па-ра-па-дам'
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:                               # проверка на количество фраз, чтобы их во фразе было >1
    print('Количество фраз должно быть больше одной!')
else:
    countVowels = []

for i in phrases:                                                  # # list.comprehension
    countVowels.append(len([x for x in i if x.lower() in vowels])) 
# print(countVowels)                                               # [4, 3, 4]
# print(countVowels[0])                                            # 4
# print(len(countVowels))                                          # 3
# print(countVowels.count(countVowels[0]))                         # 2
if countVowels.count(countVowels[0]) == len(countVowels):
    print('Парам пам-пам')
else:
    print('Пам парам')

'''
список.comprehension

for i in phrases:
    countVowels.append(len([x for x in i if x.lower() in vowels]))

если разложить строки list.comprehension, то в обычном виде код будет выглядеть так

for i in phrases:
    list=[]
    for x in i:
        if x.lower() in vowels:
        list.append(x)            # list = ['a','a','a']
            
    countVowels.append(len(list)

    
countVowels.append(len([x for x in i if x.lower() in vowels]))
эта строка звучит: в список countVowels, добавляем длину списка.comprehension 
в которые сохраняем те буквы, которые есть в списке vowels
'''