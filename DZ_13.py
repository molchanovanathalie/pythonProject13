# 1.Создайте функцию, которая запрашивает числовые данные от
# пользователя и сравнивает пока эти числа не совпадут. 5 попыток
# поисковое число случайно в заданных пределах
# Обрабатывайте не числовые данные, как исключения.

# import random
#
# def search_number(massage: str) -> int:
#     while True:
#         try:
#             return int(massage)
#         except:
#             print("Неверный формат поискового числа")
#             exit()
#
# def get_number():
#     i = 0
#     exit = 0
#     try:
#         max = int(input('введите максимальное значение поискового числа ' ))
#         min = int(input('введите минимальное значение поискового число ' ))
#         rand_num = random.randint(min, max)
#         get = search_number(rand_num)
#     except:
#         print("Неверный формат поискового числа")
#         exit()
#
#     while i < 5 and exit == 0:
#         try:
#             num = input("введите число: ")
#             res = int(num)
#
#             if get == res:
#                 print('число найдено: ', res )
#                 exit = exit + 1
#             else:
#                 print('Неверно, осталось', 4 - i, ' попыток')
#                 i = i + 1
#
#         except:
#             print("Неверный форматв ввода")
#             print('осталось', 4 - i, ' попыток')
#             i = i + 1
#
#
#
# if __name__ == '__main__':
#     get_number()
#


# ______________________________________________________________
# 2.Создайте функцию генератор чисел Фибоначчи

def fib(n):
    res_out = [0, 1]
    try:
        num = int(n)
    except:
        print("Неверный формат ввода")
        exit()
    for i in range(num):
        sum = res_out[i] + res_out[i+1]
        res_out.append(sum)
    return res_out

if __name__ == '__main__':
    n = input('введите число для генератора: ')
    print(fib(n))