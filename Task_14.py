# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число N: '))
num = 2
flag = False
if n >= 1: 
    print(1)
    flag = True
while num <= n:
    print(num)
    num *= 2
if not flag: print('Введено некорректное значение')