''''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''

def numb_pow(number, number_pow):
    if number_pow == 0:
        return 1
    elif number_pow < 0:
        return 1 / numb_pow(number, -number_pow)
    else:
        return number * numb_pow(number, number_pow - 1)

number_one = int(input('Число: '))
number_two = int(input('Степень: '))
print(numb_pow(number_one, number_two))

