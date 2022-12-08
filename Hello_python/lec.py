#colors = ['red', 'green', 'blue']
#data = open('file.txt', 'w')
# открываем файл ('путь к файлу', 'a' - для добавления/ 'r' - для чтения/
# 'w' - для записи(при этом старые записи на файле удалятся))
#data.writelines(colors) # разделителей не будет
#import os
# data.write(os.linesep + 'LINE') #еще вот так можно переходить на другую строку
# data.write(os.linesep + 'LINE')
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close

# Второй вариант открытия файла:
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
# close не нужен, т. к. после выполнения блока будет автоматический
# разрыв связи переменной data и файла

#exit() # функция exit() позволяет не выполнять последующий код

# # Выводим в консоль все строки файла
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# # У нас стоит переход на новую строку, и сам print делает переход на новую строку, отсюда задвоение пустой строки
# data.close

# import hello # импортируем из другого файла, который у нас есть
# print(hello.f(1)) # используем функцию из другого файла

# # Чтобы не писать всё время hello можно сделать так:
# import hello as h
# print(h.f(1))

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # выдаст ошибку, так как нет второго аргумента

# Но можно сделать так:
# def new_string(symbol, count = 3): # тогда по умолчанию count = 3
#     return symbol * count

# print(new_string('!')) # !!!
# print(new_string(4)) # 12
# аргументов по умолчанию может быть сколько угодно,
# но описываются в функции они самыми последними

# Чтобы указать в функции неограниченное кол-во аргументов
# нужно поставить * перед аргументом:

# def sumstring(*params):
#     res: str = ''
#     # явно указываем тип переменной. для чисел: res: int = 0
#     # указание типа необязательно, можно просто res = 0 или res = '0'
#     for item in params:
#         res += item
#     return res

# print(sumstring('a', 's', 'd', 'w')) # asdw
# print(sumstring('a', '1', 'd', '2')) # a1d2
# # print(sumstring(1, 2, 3, 4)) # type error. Тип int

# Рекурсия:
# Числа фибоначи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# lst = []
# for e in range(1, 10):
#     lst.append(fib(e))
# print(lst)


# Кортежи (неизменяемые списки):
# a, b = 3, 4 # множествен. присваивание. a = 3, b = 4

# a = (1, 2, 41, 6)
# print(a)
# print(a[0])
# print(a[-2])
# # a[0] = 12 # error. Нельзя присваивать новые значения

# t = ()
# print(type(t)) # tuple
# t = (1,) # обязательно запятая, а то будет int, а не tuple
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors) # делаем список кортежем
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# #t[0] = 'black' ## TypeError: 'tuple' object does not support item assignment

# t = tuple(['red', 'green', 'blue']) # конвертируем список в кортеж
# red, green, blue = t # распаковываем кортеж на отдельные переменные
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

# Словари: неупорядоченные коллекции произвольных объектов
# с доступом по ключу

# dictionary = {} # задаем пустой словарь
# # обратный слэш переносит на новую строку, а то строка получится очень длинная
# dictionary = \
#  {
#  'up': '↑', # up - ключ, стрелочка вверх - значение
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться

# dictionary['left'] = '⇐' # присвоили ключу другое значение
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type', несуществующий ключ
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →
# for k in dictionary.keys():
#     print(k) # выведет все ключи
# for v in dictionary.values():
#     print(v) # выведет все значения

# Множества (неупорядоченная совокупность элементов)

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21]) # конвертировали список
# c = set((2, 5, 8, 13, 21)) # конвертировали кортеж
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1} так как объекты могут быть только уникальными

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # не добавится, такой уже есть
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # удаление объекта
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# # # если попробовать удалить объект которого нет в множестве, выдаст ошибку
# colors.discard('red') # а вот такой способ удаления, даже если объекта нет, ошибку не выдаст
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } очистить множество
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} создать мн. на основе имеющегося
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединили множества
# i = a.intersection(b) # i = {8, 2, 5} пересечение множеств
# dl = a.difference(b) # dl = {1, 3} разница a от b
# dr = b.difference(a) # dr = {13, 21} разница b от a
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# #  {1, 21, 3, 13}

# # Неизменяемые множества
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# Более глубокая теория по спискам:

#list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e) # 1 2 3 4 5

# print() # вывод пустой строки

# for e in list2:
#     print(e) # 1 2 3 4 5

# list1[0] = 123 # поменяли значение в первом списке

# for e in list1:
#     print(e) # 123 2 3 4 5

# print()

# for e in list2:
#     print(e) # 123 2 3 4 5 (во втором значение тоже меняется и наоборот)

# # Поэтому не стоит так копировать списки!

# pop удаляет последний элемент списка
# print(list1.pop()) # 5 (удаляется)
# print(list1) # [1, 2, 3, 4]

# # Если нужно удалить любой другой элемент, пишем его индекс:
# print(list1.pop(2)) # 3 (удаляется)
# print(list1) # [1, 2, 4]

# # Чтобы добавить элемент на определенное место:
# print(list1.insert(2, 11)) # 2 - индекс, 11 - элемент, к-ый хотим добавить
# print(list1) # [1, 2, 11, 4]

# Если хотим добавить в конец, просто используем appened