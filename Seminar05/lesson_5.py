# num = int(input("Введите номер числа Фибоначи: "))
# def fibo(num):
#     if num == 1:
#         return 1
#     elif num == 0:
#         return 0
#     else:
#         return fibo(num - 1) + fibo(num - 2)

# print(fibo(num))


# Хакер Василий получил доступ к классному журналу и хочет заменить
# все свои минимальные оценки на максимальные. Напишите программу
# которая заменяет оценки Василия ,но наоборот: все максимальные -
# на минимальные.

import random

# list_1 = [random.randint(1, 5) for i in range(10)]
# print(list_1)

# max_count = max(list_1)
# min_count = min(list_1)

# for i in range(len(list_1)):
#     if list_1[i] == max_count:
#         list_1[i] == min_count
# print(list_1)

# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым.
# number = int(input("Введите число :"))

# def simple (num: int):
#     if not num % 2 and num != 2:
#         for dev in range (3, num//2, 2):
#             if not num % dev:
#                 return False
#     return True
# print(simple(number))

# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке. В 
# программе запрещается использовать массивы и циклы.

string = 'Привет'

print(string[::-1])


