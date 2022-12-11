# 1. Задайте строку из набора чисел. Напишите программу, которая
#    покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# def max_min_num_of_str():
#     s = input('Введите числа: ').split()
#     num = []
#     for i in range(len(s)):
#         num.append(int(s[i])) 
#     print(f'max = {max(num)}, min = {min(num)}')

# max_min_num_of_str()

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1.	с помощью математических формул нахождения корней квадратного уравнения
# 2.	с помощью дополнительных библиотек Python

# f = "5x^2+3x+-7=0"
# f = f[:-2]
# f = f.split("+")
# list = []
# for i in f:
#     list.append(int(i.split("x")[0]))
# a, b, c = list
# d = b**2 -4 * a * c
# print(d)
# if d>0:
#     x1 = round((-b - d**0.5)/(2*a), 2)
#     x2 = round((-b + d**0.5)/(2*a), 2)
#     print (x1, x2)
# elif d == 0:
#     x1 = (-b)/(2*a)
#     print(x1)
# else:
#     print('Корней нет')

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
#    этих двух чисел.

# a = int(input('Задайте число: '))
# b = int(input('Задайте второе число: '))
# if a > b:
#     for i in range (1, b+1):
#         if a * i % b == 0:
#             print(a*i)
#             break
# elif a<b:
#     for i in range (1, a+1):
#         if b * i % a == 0:
#             print(b*i)
#             break
# else:
#     print (a)

# 4. В единственной строке записан текст. Для каждого слова из данного текста
#    подсчитайте, сколько раз оно встречалось в этом тексте ранее.
#    Словом считается последовательность непробельных символов идущих подряд,
#    слова разделены одним или большим числом пробелов или символами конца строки.

# Входные данные	          Выходные данные
# one two one tho three      	0 0 1 0 0

# slovar = {'login': 'ivan', 'password': '123'}
# login = 'ivan'
# password = '12а3'
# if login == slovar['login'] and password == slovar['password']:
#     print('Доступ разрешен')
# else:
#     print('Неверная пара логин/пароль')


# slovar['email'] = 'iv@mail.ru'
# print(slovar)
# for key, value in slovar.items():
#     print(key, value)

# stroka = 'aabbbccccc' # {'a': 2, 'b': 3, 'c': 5}
# slovar = {}
# for i in stroka:
#     slovar[i] = slovar.get(i, 0) + 1
#     # if i in slovar:
#     #     slovar[i] += 1
#     # else:
#     #     slovar[i] = 1
# print(slovar)

# stroka = "one two one tho three".split()
# slovar = {}
# for i in stroka:
#     slovar[i] = slovar.get(i, -1) + 1
#     print(slovar[i],end=" ")

# 5. Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом
#    к парному ему слову. Все слова в словаре различны.
#    Для слова из словаря, записанного в последней строке, определите его синоним.

# Входные данные	Выходные данные
# 3                       Bye
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye

# slovar = {}
# for i in range (3):
#     key, value = input().split()
#     slovar[key] = value
# print(slovar)
# a = input('введите слово')
# for key, value in slovar.items():
#     if a == key:
#         print(value)
#     elif a == value:
#         print(key)

# 6. Дан текст: в первой строке задано число строк, далее идут сами строки.
#    Выведите слово, которое в этом тексте встречается чаще всего.
#    Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Входные данные	                  Выходные данные
# 1
# apple orange banana banana orange	        banana

# slovar = {}
# stroka = "apple orange banana banana orange".split(" ")
# for i in stroka:
#     slovar[i] = slovar.get(i, 0) + 1
# print(slovar)
# maxi = max(slovar.values())
# mini = "z"
# for key, value in slovar.items():
#     if value == maxi:
#         if key < mini:
#             mini = key
# print(mini)