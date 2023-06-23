# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# Решение, если числа в массиве идут от 1 до n по порядку
# x = int(input())
# array = []
# for i in range(1, x+1):
#     array.append(i)
#     print(array[i-1], end = ' ')
# print()
# y = int(input())
# if y >= array[x-1]:
#     print(array[x-1])
# elif y <= array[0]:
#     print(array[0])
# else:
#     print(y)

# Решение, если числа в массиве стоят рандомные числа от 1 до 100 (можно изменить) или рандном заменить на инпут для ввода с клавиатуры
from random import randint
x = int(input())
array = []
for i in range(1, x+1):
    array.append(randint(1,100))
    print(array[i-1], end = ' ')
print()
y = int(input())
deff = abs(array[0] - y)
deff_values = array[0]
for i in array:
    if deff > abs(i - y):
        deff = abs(i - y)
        deff_values = i
print(deff_values)