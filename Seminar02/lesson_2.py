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
     
import random