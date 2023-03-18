# def f(x):
#     return x*x
# print(f(5))

# def calk_1(a, b):
#    return a + b

# def calk_2(a, b):
#    return a * b

# def math(op, x, y):
#     print(op(x, y))
    
# math(calk_2, 5, 45)

# calk_1 = lambda a, b: a + b

import random 
# n = int(input("Введите длину списка:"))
# list_1 = [random.randint(1, 20) for i in range(n)]
# print(list_1)
# new_list = []
# finish_list = []
# for i in list_1:
#     if i % 2 == 0:
#         new_list.append(i)
# print(new_list)
# result = 1
# for i in new_list:
#      result = i * i
#      finish_list.append(result)
#      result = 1
# print(finish_list)

# n = int(input("Введите длину списка:"))
# list_1 = [random.randint(1, 20) for i in range(n)]
# print(list_1)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]
           
# list_1 = where(lambda x: x % 2 == 0, list_1)
# print(list_1)
# list_1 = (select(lambda x: (x, x **2), list_1))
# print(list_1)

# list_1 =[i for i in range(1,20)]
# print(list_1)
# list_1 = list(map(lambda i: i + 10, list_1))
# print(list_1)

# list_1 = "12 76 27 2 7 798 29"
# list_1 = list(map(int, list_1.split()))
# print(list_1)

# list_1 = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, list_1))
# print(res)