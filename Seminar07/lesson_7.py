# transformation = lambda x: x

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# def find_farthest_orbit(orb):
#     new_orb = list(filter(lambda x: x[0] != x[1], orb))
#     # for i in orb:
#     #     if i[0] != i[1]:
#     #         new_orb.append(i)
#     return max(new_orb, key = lambda x: x[0] * x[1])
            
        

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# my_string = '12427146712461'
# my_string = list(my_string)
# print((my_string))

# my_string = list(map(int, my_string)) # Приведение типа данных списка 
                                      # из строки в числа(функцией map)
                                      # первый аргумент тип данных
                                      # второй , что хотим привести.

# my_string = '12427146712461'
# my_string = list(my_string)
# my_string = list(map(lambda x: int(x), my_string)) # Лямбда функция.

# my_string = list(filter(lambda x: x % 2 == 0, my_string))
# # фильтр по четным числам.

# my_string = [int(x) for x in my_string if int(x) % 2 == 0]
# # List comprehation

# my_string = 'shdjsahdjash'
# my_string = list(my_string)

# for i, item in enumerate(my_string): # нумерация списка
#     print(f'{i}. {item}')
    
# my_string = 'shdjsahdjash'
# my_list = [i for i  in range(10)]
# my_string = list(my_string)
# print(my_string)
# print(my_list)
# new_list = list(zip(my_string, my_list))
# print('')
# print(new_list)

