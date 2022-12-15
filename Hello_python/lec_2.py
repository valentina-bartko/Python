# Ускоренная обработка данных:
# lambda, filter, map, zip, enumerate, List Comprehension 

# Допустим, у нас есть две функции, одна прибавляет к числу 10,
# вторая возводит число в степень
# def sum(x):
#     return x+10
# def mult(x):
#     return x**2
# sum(mult(2)) # 2**2 + 10 = 14

# Предположим, что какая-то функция нам понадобится только один раз
# за всю работу приложения. Можно ли как-то обойтись без использования
# явного описания функции?

# Функция имеет тип function
# И её можно положить в другую переменную:

# def f(x):
#     return x**2
# g = f # Теперь мы можем вызывать g, и она будет работать как фунция f
# print(g(4)) # 16

# Допустим у нас есть функция которая умножает

# def calc2(x):
#     return x * 10

# # Теперь создадим функцию, которая в качестве аргументов будет брать
# # другую функцию и число:
# def math(op, x):
#     print(op(x))
# math(calc2, 10) # 10**2 = 100

# Также это будет работать и с большим количеством аргументов:
# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))

# # calc(mylt, 4, 5) # 20

# # Всё это можно записать более красиво (с помощью lambda):
# sum = lambda x, y: x * y
# calc(sum, 3, 4) # 12
# # Можно пропустить и этап присваивания к переменной:
# calc(lambda x, y: x * y, 3, 4) # 12



# List Comprehension (быстрое создание списков):
# [exp for item in iterable] # Если нужно пройтись по списку
# [exp for item in iterable (if conditional)] # Если нужно ещё и проверить условие
# [exp <if conditional> for item in iterable (if conditional)]

# Допустим мы хотим создать список чётных чисел в диапазоне от 1 до 100:
# lst = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)

# Теперь сделаем это более красиво (пока без условия):
# lst = [i for i in range(1, 101)]
# print(lst) # [1, 2, 3, 4, 5, ...]

# Добавим условие:
# lst = [i for i in range(1, 101) if i % 2 == 0]
# print(lst) # [2, 4, 6, 8, ...]

# Если нам нужно выводить кортежи:
# lst = [(i, i) for i in range(1, 101) if i % 2 == 0]
# print(lst) # [(2, 2), (4, 4), (6, 6), ...]

# Теперь в качестве i передадим функцию:
# def f(x):
#     return x ** 2
# lst = [f(i) for i in range(1, 101) if i % 2 == 0]
# # То есть сначала из диапазона выбираются только чётные числа,
# # а затем к ним применяется функция возведения в квадрат
# print(lst) # [4, 16, 36, 64, 100, ...]

# Для большей наглядности подключим кортежи (пара: число, квадрат)
# def f(x):
#     return x ** 2
# lst = [(i, f(i)) for i in range(1, 101) if i % 2 == 0]
# print(lst) # [(2, 4), (4, 16), (6, 36), ...]

# Вернёмся к lambda
# Задача (почти такая же):
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# Я создала файл с этими числами через пробел
# path = 'numbers.txt' # Положили файл в переменную path
# f = open(path, 'r') # Открыли файл в режиме чтения
# data = f.read() + ' '
# # В переменную data положили эту строку из файла с добавленным в конце пробелом
# f.close()

# numbers = []

# while data != '': # До тех пор пока data не пустая строка
#     space_pos = data.index(' ') # Положили в space_pos индекс первого пробела
#     numbers.append(int(data[:space_pos]))
#     # Добавили в список все, что идет до пробела (конвертировав в число)
#     data = data[space_pos+1:] # Теперь в дату положили всё, что идет после этого пробела

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

# Можно ли сделать этот код лучше?

# Создадим функ. select, которая будет принимать функцию и какой-то набор данных
# def select(f, col):
#     return [f(x) for x in col]
#     # Создаем новый список, в котором будут элементы входного списка,
#     # к которым была применена входная функция

# def where(f, col):
#     return [x for x in col if f(x)]
#     # Создаем новый список, в котором будут элементы входного списка,
#     # подходящие под условие

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data) # Теперь в res лежит список конверт. подстрок из data
# res = where(lambda x: not x % 2, res) # Теперь лежат только четные
# res = select(lambda x: (x, x**2), res) # Тепрь кортежи из числа и квадрата
# print(res)


# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами
# li = [x for x in range(1,20)] # Создаем список [1, 2, 3, ..., 19]
# li = list(map(lambda x: x + 10, li))
# # Обязательно ставим list в начале, чтобы принудительно сохранить
# новые данные
# print(li) # [11, 12, 13, ..., 29]

# Задача: ввести строку с клавиатуры и преобразовать в числовой список
# data = list(map(int, input().split()))
# print(data)

# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data)) # В качестве функции идет условие
# print(res)

# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора

# users = ['user 1', 'user 2', 'user 3', 'user 4']
# ids = [4, 7, 11, 13]

# data = list(zip(users, ids))
# # Первый элемент первого списка с первым элементом второго списка,
# # второй элемент первого со вторым элементом второго и т. д.
# print(data)
# Если бы допустим у нас был третий список из трёх элементов,
# и мы тоже закинули его в zip, вывелся бы список только из трёх кортежей

# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных

users = ['user 1', 'user 2', 'user 3', 'user 4']
data = list(enumerate(users))
print(data) # [(0, 'user 1'), (1, 'user 2'), (2, 'user 3'), (3, 'user 4')]