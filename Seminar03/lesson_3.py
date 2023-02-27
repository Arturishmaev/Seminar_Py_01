# import random
# list_1 = [random.randint(0, 100) for i in range(10)] # Рандомный 
# # генератор случайных элементов от 0 до 99 , 10 элементов.

# for item in list_1:
#     print(item)    # Проход по элементам.


# for i in range(len(list_1)):
#     print(list_1[i])  # Проход по индексам. 
    
# dict_1 = {1: 'one', 2: 'two', 3: 'three'} # Создание словаря, где 
# # цифры - это ключи, слова - значения. Ключи не должны повторятся.
# dict_1[4] = 'four' # Добавление значения в словарь.

# print(dict_1.get(2, 'такого значения нет')) # Вывести второй ключ словаря.
# # Если указать несуществующий ключ, вместо ошибки: 'такого значения нет'
import random
# my_list = [random.randint(0, 10) for i in range(20)]
# print(my_list)

# new_list = []
# for item in my_list: # Для добавления в new_list без повторений
#     if item  not in new_list:
#         new_list.append(item)
# print(new_list)
# print(len(new_list))

# my_list = [random.randint(0, 10) for i in range(20)]
# print(my_list)
# print(set(my_list))
# print(len(set(my_list)))

# Дана последовательность из n чисел и число k. Необходимо сдвинуть всю
# последовательность на k элементов вправо, k - положительное число.
# n = int(input("Введите количество элементов : "))
# my_list = [random.randint(0, 10) for i in range(n)]
# print(my_list)
# k = int(input("Сдвиг вправо (шаг): "))
# for i in range(k):
#     my_list.insert(0, my_list.pop(-1)) # значение с последнего индекса(pop-1)
#                                        # перносим на нулевой индекс.insert(0,
    
# print(my_list)

# Задать список из рандомных чисел , создать новый список только с 
# уникальными значениями.

# my_list = [random.randint(0, 10) for i in range(10)] # Рандомный список
# print(my_list)
# my_dict = {}  # Пустой словарь

# for item in my_list: # Проход по элементам списка.
#     my_dict[item] = my_dict.get(item, 0) + 1 # Создаем новый ключ.
# print(my_dict)

# new_list = []

# for key, value in my_dict.items():
#     if value == 1:
#         new_list.append(key)
# print(new_list)
# Лучшее решение:

my_list = [random.randint(0, 10) for i in range(10)]   
print(my_list)
new_list = [] 
for item in my_list: # item - элементы
    if my_list.count(item) == 1: # count - кол-во повторений, если = 1,
        new_list.append(item) # то добавляет его в new_list
        
print(new_list)



