# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]  

# sp = ['привет', 'забвение', 'пока']
# sp = filter(lambda x: 'абв' not in x, sp)
# print(list(sp))

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 121 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# ОТВЕТ: Первому  игроку  надо первым ходом забрать остаток от целочисленного деления
# имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1
# В дальнейшем первому игроку нужно повторять стратегию, хотя без калькулятора не всегда это удобно посчитать))))
# Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
# если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19 и так далее..
# Это как реализовано в игре против компа, хотя я прау раз выиграл, видимо не совсем правильно работает(((((


# from random import *
# import os


# welcome_text = ('Приветствую Вас, маленькие любители сладкого!\n'
#                 'Хотите сыграть в игру "2021 шаг в сторону сахарного диабета"?\n'
#                 'Для начала я расскажу правила:\n'
#                 'Я даю Вам 2021 конфету, вы берете их поочереди,\n'
#                 'причем, за один раз можно взять не больше 28 конфет.\n'
#                 'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
#                 'Ну что начнем?')
# print(welcome_text)

# message = ['твоя очередь', 'да бери уже', 'бери больше', 'не корову проигрываешь',
#            'бери быстрее', 'да харош, так долго думать уже']


# def player_vs_player():
#     candies_total = 2021
#     max_take = 28
#     count = 0
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = input('\nА твоего соперника?: ')

#     print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     x = randint(1, 2)
#     if x == 1:
#         lucky = player_1
#         loser = player_2
#     else:
#         lucky = player_2
#         loser = player_1
#     print(f'Поздравляю {lucky} ты ходишь первым !')

#     while candies_total > 0:
#         if count == 0:
#             step = int(input(f'\n{choice(message)} {lucky} = '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nНе жадничай можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 1
#         else:
#             print('Все кончились конфетки')

#         if count == 1:
#             step = int(input(f'\n{choice(message)}, {loser} '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nНе жадничай можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 0
#         else:
#             print('Баста, карапузик, кончились конфетки')

#     if count == 1:
#         print(f'{loser} ПОБЕДИЛ')
#     if count == 0:
#         print(f'{lucky} ПОБЕДИЛ')


# player_vs_player()


# def player_vs_bot():
#     candies_total = 2021
#     max_take = 28
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = 'Компьютер'
#     players = [player_1, player_2]
#     print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     lucky = randint(-1, 0)

#     print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step

#     print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()



# 3. Создайте программу для игры в "Крестики-нолики".

# board = list(range(1,10))

# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(board)

# # 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Некорректно работает

# def encode(file_1, file_2, stop_pos):
#     with open(file_1, 'r') as data:
#         with open(file_2, 'a') as data_2:
#             data = data.read()
#             s = ''
#             num = 0
#             for i in range(stop_pos, len(data)):
#                 s = data[i]
#                 if i + 1 == len(data):
#                     return
#                 elif data[i] == data[i + 1]:
#                     num += 1
#                 else:
#                     num = str(num)
#                     data_2.write(s + num)
#                     stop_pos = i + 1
#                     return


# global stop_pos
# stop_pos = 0

# with open('text_to_encode.txt', 'w') as data:
#     data.write(input('Введите текст для кодировки: '))
   
# with open('text_to_encode.txt', 'r') as data:
#     data = data.read()
#     length = len(data)

# while stop_pos < length - 1:
#     encode('text_to_encode.txt', 'encoded_text.txt', stop_pos)

# # Неккоректно работает