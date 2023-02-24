# number = int(input("Введите число N :"))

# i = 1
# factorial = 1
# while i <= number:
#     factorial *= i
#     i += 1
# print(f"Факториал из числа {number} = {factorial}")

# Дано натуральное число A > 1.Определите, каким по счету числом Фибоначчи
# оно является, т.е. выведите такое число n , что ф(n) = A.
# Если А не является числом Фибоначчи, выведите -1.

# number = int(input("Введите предел: "))
# fibo1 = 0
# fibo2 = 1
# fibo_cur = 0
# count = 1

# while fibo_cur < number:
#     fibo_cur = fibo1 + fibo2
#     fibo1, fibo2 = fibo2, fibo_cur
#     count += 1

# print(count if number == fibo_cur else '-1')

# import random
# n = random.randint(1000, 30000)

# import random

# watermelons = int(input("Введите кол-во арбузов: "))
# max_weight = random.randint(1000, 30000)
# min_weight = max_weight
# print(max_weight)
# print("")
# for i in range(0, watermelons):
#     weight = random.randint(1000, 30000)
#     print(weight)
# if weight > max_weight:
#     max_weight = weight
# if weight < max_weight:
#     min_weight = weight
# print(f"Из {watermelons} арбуза(ов), максимальный вес = {max_weight}, минимальный вес = {min_weight}")


import random

count_day = int(input("Введите количество дней :"))
temp = 0
count = 0
count_max = 0

for i in range(count_day):
    temp += random.randint(-4, 4)
    if temp > 0:
        count += 1
    else:
        print(f"----------{count}----------")   
        count = 0 
    print(temp)  
    if count > count_max:
        count_max = count  

