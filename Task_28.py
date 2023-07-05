''''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
'''

def summ_numbers(a,b):
    if b == 0:
        return a
    a += 1
    return summ_numbers(a, b-1)

number_one = int(input('первое число: '))
number_two = int(input('второе число: '))
print(summ_numbers(number_one, number_two))