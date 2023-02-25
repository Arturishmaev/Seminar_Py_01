list_1 = [] # Создание пустого списка.
list_2 = list() # Создание пустого списка.
list_3 = [1, 2, 3, 4, 5] # * открыть список, убрать скобки, print(*list_3)

for i in list_3:
    print(i)
    
print(len(list_3)) # Длина списка.

print(list_3[0]) # Вывод элемента списка с индексом 0.

print(list_3[-1]) # Вывод последнего элемента списка ( с конца).

list_3.append(6) # Добавить цифру 6 в конец списка.

list_4 = []
for i in range(5): # i принимает значение от 1 до 4.
    list_4.append(i)  # поочередное дополнение списка i-тыми значениями.
    print(list_4) 

# [0] - пример вывода
# [0, 1]
# [0, 1, 2]      
# [0, 1, 2, 3]   
# [0, 1, 2, 3, 4]       

list_5 = [12, 7, -1, 21, 0] 
print(list_5.pop()) # удаление последнего элемента списка.
print(list_5) # [12, 7, -1, 21] 
print(list_5.pop(1)) # [12, -1, 21] удаление конкретного элемента.


list_5 = [12, 7, -1, 21, 0] 
print(list_5.insert(2, 11)) # первый аргумент(2)- номер индекса элемента.
                            # второй элемент (11)- значение элемента
print(list_5) # [12, 7, 11, -1, 21, 0]

list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_6[0])  # 1
print(list_6[1])  # 2
print(list_6[len(list_6) - 1])  # 10
print(list_6[-5])  # 6
print(list_6[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_6[:2])  # [1, 2]
print(list_6[len(list_6) - 2:])  # [9, 10]
print(list_6[2:9])  # [3, 4, 5, 6, 7, 8, 9]
print(list_6[6:-18])  # []
print(list_6[0:len(list_6):6])  # [1, 7]
print(list_6[::6])  # [1, 7]

t = () # Создание пустого кортежа.

a, b = 1, 2 # Множественное присваивание

# d = {} # Создание пустого словаря
# d = dict() # Создание пустого словаря
# d['q'] = 'qwerty'
# print(d) # {'q': 'qwerty'}

# d['w'] = 'werty' 
# print(d)  # {'q': 'qwerty', 'w': 'werty'}

# d['w'] = 'werty' 
# print(d['q'])  # qwerty

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
    
    
# 💡 Множества содержат в себе уникальные элементы, не обязательно
# упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два
# множества, Вы можете совершать над ними любые стандартные операции,
# например, объединение, пересечение и разность. Давайте разберем их.
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set() - cоздание множества.


# Операции со множествами в Python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5} - поиск одинаковых значений
dl = a.difference(b) # dl = {1, 3} - исключение всех повторяющихся значений
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset) — множество, с которым
# не будут работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

# List Comprehension
# У каждого языка программирования есть свои особенности и преимущества. Одна
# из культовых фишек Python — list comprehension (редко переводится на русский, но
# можно использовать определение «генератора списка»). Comprehension легко
# читать, и их используют как начинающие, так и опытные разработчики.
# List comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке  

# 1. Простая ситуация — список:
list_1 = [exp for item in iterable]
# 2. Выборка по заданному условию:
list_1 = [exp for item in iterable (if conditional)]

# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]

# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]

#Также можно умножать, делить, прибавлять, вычитать. Например, умножить
#значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]

# 🔥 Самые распространенные ошибки:

 ● SyntaxError(Синтаксическая ошибка)
number_first = 5
number_second = 7
if number_first > number_second # !!!!!
print(number_first)
# Отсутствие :

● IndentationError(Ошибка отступов)
number_first = 5
number_second = 7
if number_first > number_second:
print(number_first) # !!!!!
# Отсутствие отступов

● TypeError(Типовая ошибка)
text = 'Python'
number = 5
print(text + number)
# Нельзя складывать строки и числа

● ZeroDivisionError(Деление на 0)
number_first = 5
number_second = 0
print(number_first // number_second)
# Делить на 0 нельзя

● KeyError(Ошибка ключа)
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[3])
# Такого ключа не существует

● NameError(Ошибка имени переменной)
name = 'Ivan'
print(names)
# Переменной names не существует

● ValueError(Ошибка значения)
text = 'Python'
print(int(text))
# Нельзя символы перевести в целые значения
