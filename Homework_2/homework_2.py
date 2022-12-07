# ЗАДАЧА № 1
# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# o	6782 -> 23
# o	0.56 -> 11

# a = list(input('Введите вещественное число: '))
# sum = 0
# for i in a:
#     if i != '.':
#         sum += int(i)
# print(sum)

# ЗАДАЧА № 2

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# o	пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# n = int(input('Введите число: '))
# lst = []

# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n-1) * n

# for i in range(1, n+1):
#     lst.append(factorial(i))

# print(lst)

# ЗАДАЧА № 3
# Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.

# n = int(input('Введите число: '))
# sum = 0

# for i in range(1, n+1):
#     sum += (1+1/n)**2
# print(sum)

# ЗАДАЧА № 4
# Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random
# n = int(input('Введите число N: '))
# lst = []

# for i in range(n+1):
#     lst.append(random.randint(-n, n+1))
# print(lst)

# f = open('positions.txt', 'w')
# while True:
#     pos = input('Укажите позицию для вычисления: ')
#     if pos == "":
#         break
#     f.write(pos+"\n")
# f.close()

# f = open('positions.txt', 'r')
# res = 1
# for line in f:
#     if line == "":
#         break
#     res *= lst[int(line)]
# f.close()
# print(f'Произведение чисел на этих позициях = {res}')


# ЗАДАЧА № 5
# Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).

# import random
# lst = [4, 7, 2, 9, 5, 1]
# print(f'Начальный список: {lst}')
    
# for i in range(len(lst)-1, 0, -1):
#     j = random.randint(0, i + 1)
#     lst[i], lst[j] = lst[j], lst[i]
# print(f'Перемешанный список: {lst}')