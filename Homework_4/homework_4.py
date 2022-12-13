# 1. Вычислить число c заданной точностью d
# Пример:
# o	при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

# import math
# d = input('Введите число d: ')
# if len(d) > 2 and len(d) < 13:
#     d = d.split('.')
#     res = str(round(math.pi, len(d[1]) + 1))
#     print(res[:-1])
# else:
#     print('Число d не соответствует условиям:')
#     print('10^{-1} ≤ d ≤10^{-10}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список
#    простых множителей числа N.

# n = int(input('Введите натуральное число N: '))
# sp = []

# def division(n):
#     for i in range(2, 10):
#         if n % i == 0:
#             sp.append(i)
#             n = int(n / i)
#             division(n)
#     if n != 1:
#         sp.append(n)
#     print(sp)

# division(n)
# В консоль выведется сразу несколько списков из-за рекурсии,
# ответ задачи - это первый список.
# Я не смогла найти ответ как выводить значение только последней рекурсии.

# 3. Задайте последовательность чисел. Напишите программу, которая
#    выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4]  -> [1, 3, 4]

# lst = list(input('Введите числа через пробел: ').split())
# sp = []
# for i in lst:
#     if lst.count(i) == 1:
#         sp.append(i)

# print(sp)

# 4. Задана натуральная степень k. Сформировать случайным образом
#    список коэффициентов (значения от 0 до 100) многочлена и записать
#    в файл многочлен степени k.
# Пример:
# o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#import random
#k = int(input('Введите натуральную степень k: '))

def coefficients(k):
    num = []
    for i in range(k+1):
        num.append(random.randint(0, 100))
    return num


def equation(num):
    str = ''
    for i in range(len(num)):
        if i != len(num) - 1 and i != len(num) - 2 and num[i] != 0:
            str += f'{num[i]}x^{len(num) - i - 1}'
            if num[i+1] != 0:
                str += ' + '
        elif i == len(num) - 2 and num[i] != 0:
            str += f'{num[i]}x'
            if num[i+1] != 0:
                str += ' + '
        elif i == len(num) - 1 and num[i] != 0:
            str += f'{num[i]} = 0'
        elif i == len(num) - 1 and num[i] == 0:
            str += ' = 0'
    return str

def file(fale_name, str):
    with open(fale_name, 'w') as data:
        data.write(str)

#file('equat.txt', equation(coefficients(k)))

# 5. Даны два файла, в каждом из которых находится запись многочлена.
#    Задача - сформировать файл, содержащий сумму многочленов.
# (Методы из предыдущей задачи.)

# import random
# k = 2

# def copying_str(file_name):
#     equation = ''
#     with open(file_name, 'r') as data:
#         equation += data.readline()
#     return equation

# def removal_of_excess(st):
#     for char in 'x^+=':
#         st = st.replace(char, ' ')
#     ls = st.split()
#     delete = ls.pop(1)
#     delete = ls.pop()
#     ls = [int(item) for item in ls]
#     return(ls)

# def create_file_sum(ls_1, ls_2):
#     res = []
#     for i in range(0, 3):
#         res.append(ls_1[i] + ls_2[i])
#     res_equation = f'{res[0]}x^2 + {res[1]}x + {res[2]} = 0'
#     with open('res_eq', 'w') as res_eq:
#         res_eq.write(res_equation)

# file('eq_1.txt', equation(coefficients(2)))
# file('eq_2.txt', equation(coefficients(2)))
# sp_1 = copying_str('eq_1.txt')
# sp_2 = copying_str('eq_2.txt')
# ls_1 = removal_of_excess(sp_1)
# ls_2 = removal_of_excess(sp_2)
# create_file_sum(ls_1, ls_2)