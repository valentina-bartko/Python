print('hello world') #нет точки с запятой
a = 123 #необязательно указывать тип данных
b = 1.23 
print(a)
print(b)
value =  None  #нельзя просто объявить переменную, но можно присвоить ей временное значение None
print(type(value))

value = 12334
print(value)
print(type(a)) #чтобы посмотреть какой тип данных содержит переменная
print(type(b))
print(type(value))

s = 'hello world' #строка
print(s)
s = "hello 'world'" #если в самой строке нужны одинарные кавычки, просто добавляем двойные кавычки и наоборот
print(s)
s = "hello \'world\'" #второй вариант: ставим перед кавычками обратный слэш
s = 'hello \nworld' #с помощью \n делаем переход на новую строку
print(s)

print(a, 'lala', b, 'tytyty', s) #вывод в консоль
print('{} - {} - {}'.format(a, b, s)) #форматирование
print(f'{a} - {b} - {s}') #или более простой вариант
print('{2} - {1} - {0}'.format(a, b, s)) #так их можно менять местами

f = True # логический тип данных
d = False
print(f, d)

# в python нужно быть очень аккуратным с пробелами

#list = [1, 2, 3, 'juk', 'hio', 5.87, True] # массив задается просто квадратными скобками
#print(list)

#print('Введите a')
#a = input()  #ввод данных пользователем
#print('Введите b')
#b = input()
#print(a, b)
#print('{} {}'.format(a, b))
#print(f'{a} {b}')

#print(a, '+', b, '=', a + b) # по умолчанию выведется строка (1+2 будет 12, а не 3)
# чтобы этого не было, перед input пишем int/float/другой тип, который нам нужен
#print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a + b)

a = 12
b = 5
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b # вывод будет вещественным числом
print(c)
c = a // b # вывод в целых числах
print(c)
c = a % b # остаток от деления
print(c)
c = a ** b # возведение в степень
print(c)

a = 1.344
b = 7
c = a * b
print(c) # выводится слишком длинное число
c = round(a*b)
print(c) # округлилось до целых
c = round(a*b, 3)
print(c) # округлилось до трёх знаков после запятой

a = 3
a = a + 5
print(a)
# или
a = 3
a += 5
print(a)
a -= 5
a *= 5
# и так далее

# логические операции
# <, <=, >, >=, ==, !=
# not, and, or 
# is, is not, in, not in
a = 1 < 4
print(a) # true
a = 1 > 4
print(a) # false
a = 1 < 4 and 5 < 2
print(a) # false

a = 4
b = 6
c = 9
print(a<b<c) # тройные (и больше) неравенства

f = 1 < 2 or 4 < 6 # true
print(f)

y = [1, 2, 3]
print(y)
print(2 in y) # получаем true, так как 2 есть в списке
print(not 2 in y) # false

is_odd = y[0] % 2 == 0 # проверяем четность числа
print(is_odd)
is_odd = not y[0] % 2 # тут отрицание единицы (более корректный вариант записи)
print(is_odd)

# if, if-else
# a = int(input('a =')) # вот так еще можно запрашивать данные у пользователя
# b = int(input('b ='))
# if a > b:
#     print(a) # отступы очень важны
# else:
#     print(b)

# if, elif, else
# username = input('Введите имя: ')
# if username == 'Валя':
#     print('Ура, это же ВАЛЯ!')
# elif username == 'Данил':
#     print('Я так ждала тебя, Данил')
# elif username == 'Руся':
#     print('Руся - топ')
# else:
#     print('Привет,', username)

# Циклы while, for
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# так же можно добавить else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит)')
print(inverted)

#for
for i in 1, 2, 3, 4, 5:  # i - счётчик, после in идёт объект 
    print(i**2) # получили все квадраты по списку

list = [1, 2, 3, 10, 5]
for i in list:
    print(i) # вывод списка

for i in range(5):  # range выведет набор чисел от 0 до 4
    print(i)

for i in range(1, 5):  # range выведет диапазон от 1 до 4
    print(i)

for i in range(1, 10, 2): # третий аргумент - приращение (на 2)
    print(i)

text = 'съешь ещё этих мягких французских булок'
# Чтобы получить справку по незнакомой команде, пишем help(x.команда):
#help(text.istitle)

print(len(text)) # длина, кол-во символов(39)
print('ещё' in text) # есть ли там такое слово(true)
print(text.isdigit()) # проверяем все ли элементы строки являются числами(false)
print(text.islower()) # проверяем все ли символы в нижнем регистре(true)
print(text.replace('ещё', 'ЕЩЁ')) # заменяем первый аргумент на второй

print(text[0]) # c
print(text[1]) # ъ
print(text[len(text) - 1]) # к
print(text[-5]) # б
print(text[:]) # print(text). По другому это будет [0 : len(text) - 1]
print(text[2:5]) # съ
print(text[6:-18]) # ещё этих мягких


#списки
numbers = [1, 2, 3, 4, 5]
print(numbers)
#ran = range(1, 6)
#print(type(ran))
#numbers = list(range(1, 6)) #теперь в массиве range (почему-то не работает)
print(type(numbers))

print(numbers)
numbers[0] = 10
print(f'{len(numbers)} len') # 5 len
print(numbers)

for i in numbers:
    i *= 2
    print(i)
print(numbers)


# Добавление и удаление элементов

colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue

for e in colors:
    print(e*2) # redred greengreen blueblue

colors.append('gray') # Добавление элемента в конец списка
print(colors)

colors.remove('red') # Удаление элемента из списка
del colors[1] # либо же такой вариант
print(colors)

# Функции

def f(x): # def (функция), f (название функции), (x) - аргумент
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print (f(arg))
print(type(f(arg)))