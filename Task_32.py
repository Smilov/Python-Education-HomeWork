''''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

from random import randint
range_one = int(input('Введите первое число диапозона поиска(1-10):    '))
range_last = int(input('Введите последнее число диапозона поиска(1-10):    '))
my_list = [randint(0, 10) for _ in range(randint(3,10))]
print(my_list)
for i in range(len(my_list)):
    if range_one <= my_list[i] <= range_last:
        print(i, end = ' ')