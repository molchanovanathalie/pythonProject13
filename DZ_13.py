# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Дополнительно: реализуйте ввод из командной строки


import logging

logging.basicConfig(filename= 'logger.log', encoding='utf-8', level= logging.INFO, filemode='w')
logger = logging.getLogger(__name__)


# 1.Создайте функцию, которая запрашивает числовые данные от
# пользователя и сравнивает пока эти числа не совпадут. 5 попыток
# поисковое число случайно в заданных пределах
# Обрабатывайте не числовые данные, как исключения.

# import random
#
# def search_number(massage):
#     try:
#         return int(massage)
#     except Exception as se:
#         logger.error(f'Неверный формат поискового числа {se}')
#         print("Неверный формат поискового числа")
#         exit()
#
#
# def get_number():
#     i = 0
#     exit = 0
#     try:
#         max = int(input('введите максимальное значение поискового числа:  ' ))
#         min = int(input('введите минимальное значение поискового число:  ' ))
#         rand_num = random.randint(min, max)
#         get = search_number(rand_num)
#     except Exception as se:
#         print("Неверный формат  числа")
#         logger.error(f'Неверный формат числа {se}')
#         exit()
#
#     while i < 5 and exit == 0:
#         try:
#             num = input("введите число: ")
#             res = int(num)
#
#             if get == res:
#                 print('число найдено: ', res)
#                 exit = exit + 1
#                 return logger.info(f'число найдено: {res}')
#
#             else:
#                 logger.info (f'Неверно, осталось {4-i} попыток')
#                 print('Неверно, осталось', 4 - i, ' попыток')
#                 i = i + 1
#
#         except Exception as se:
#             logger.error(f'Неверный формат ввода {se} осталось {4 - i}  попытки(ка)')
#             print("Неверный формат ввода")
#             print('осталось', 4 - i, ' попыток')
#             i = i + 1
#
#
#
# if __name__ == '__main__':
#     get_number()
# #


# ______________________________________________________________

# 2.Создайте функцию генератор чисел Фибоначчи

import sys

def fib(n):
    res_out = [0, 1]
    try:
        num = int(n)
    except Exception as se:
        logger.error(f'Неверный формат ввода {se}')
        exit()
    for i in range(num):
        sum = res_out[i] + res_out[i+1]
        res_out.append(sum)
    print(res_out)
    return  logger.info(f'числа Фибоначи для {num} = {res_out}')


if __name__ == '__main__':
    DZ, n = sys.argv
    n = input('введите число для генератора: ')
    print(fib(n))


# в терминал для генератора:
# python DZ_13.py 'n'