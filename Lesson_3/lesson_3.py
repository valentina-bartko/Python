# 1. Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
#    Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# lst = [int(i) for i in input().split()] # ввод строки в консоль через пробел, разделение и конверт в int

# for i in lst:
#     if lst.count(i) == 1:
# # узнаем при помощи count, если бы вместо 1 было бы 2, он показал бы нам какие числа встречаются в списке дважды
#         print(i)

# 2. Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# Входные данные	Выходные данные
# 1 5 2 4 3	          5 4

# lst = [int(i) for i in input().split()]
# for i in range(len(lst) - 1):
#     if lst[i] < lst [i+1]:
#         print(lst[i+1], end = " ")

# 3. Реализуйте алгоритм задания случайных чисел без использования
#    встроенного генератора псевдослучайных чисел.

# Подсказка: можно использовать модуль datetime

# import time

# def my_random(x):
#     t = str(time.time())[-x:] # time.time() показывает сколько секунд прошло с x даты
# # мы конвертируем time в str и отрезаем x последних символов
#     print(t)

# my_random(2)

# 4. Задайте список. Напишите программу, которая определит, присутствует ли
#    в заданном списке строк некое число.
# Входные данные	Выходные данные
# 12                       да
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка

# a = input('Введите число: ')
# lst = []

# for i in range(5):
#     s = input()
#     lst.append(s) # наполняем список вводимыми строками
# print(lst)

# count = 0
# for i in lst:
#     if a in lst:
#         count += 1 # если a есть в lst, добавляем count

# if count >= 0:
#     print('Да')
# else:
#     print('Нет')

# 5. Напишите программу, которая определит позицию второго вхождения строки
#    в списке либо сообщит, что её нет.
# Пример:
# •	список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# •	список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# •	список: [], ищем: "123", ответ: -1

# strings = ['qwe', 'asd', 'zxc', 'qwe', 'ertwe']
# find = 'qwe'
# count = 0
# for i in range(len(strings)): # если написать не range, а strings выдаст ошибку
#     if strings[i] == find:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# if count <= 1:
#     print(-1)

# 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Входные данные	Выходные данные
# 1 5 2 2 2 4	         4

# numbers = [1, 5, 2, 2, 2, 4]
# print(len(set(numbers))) # конверт в множество, останутся только уникальные числа

# 2. Даны два списка чисел. Найдите все числа, которые входят как в первый,
#    так и во второй список и выведите их в порядке возрастания.
# Входные данные	Выходные данные
#   1 3 2
#   4 3 2	             2 3

# lst_1 = [1, 3, 2]
# lst_2 = [4, 3, 2]
# print(*set(lst_1) & set(lst_2))

# 3. Вам дан английский текст. Закодируйте его с помощью азбуки Морзе:

# Входные данные	Выходные данные
# Help me SOS
# 	               .... . .-.. .--.
#                  -- .
#                  ... --- ...
# MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#          'D': '-..', 'E': '.', 'F': '..-.',
#          'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..',
#          'M': '--', 'N': '-.', 'O': '---',
#          'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-',
#          'V': '...-', 'W': '.--', 'X': '-..-',
#          'Y': '-.--', 'Z': '--..'}

# text = input('Введите текст: ').upper().split() # upper переводит всё в верхний регистр

# for i in text:
#     for j in i:
#         if j in MORSE:
#             print(MORSE[j], end = ' ')
#         else:
#             print(j, end = ' ')
#     print()

# 4. Для каждого слова исходного текста выведите одно целое число — номер вхождения этого слова в текст.
#    Числа выведите через пробел. Количество чисел должно совпадать с количеством слов в исходном тексте.
# Входные данные	                      Выходные данные
# Раз раз раз как меня слышно            1 2 3 1 1 1 1 4 5 6 2 
#  Повторяю раз раз раз Повторяю

# text = 'Раз раз раз как меня слышно Повторяю раз раз раз Повторяю'
# text = text.lower().split()
# print(text)
# for i in text:
# Недорешала