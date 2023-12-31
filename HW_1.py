# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |



number = abs(int(input('Введите число: ')))
summ = 0
while number / 10 > 0:
    summ += number % 10
    number = number // 10
print(F'Cумма цифр заданного числа = {summ}')




# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


all_bird = int(input('Введите общее число журавликов, которые сделали дети: '))
if all_bird < 0 or all_bird % 6 != 0:
    print('Вы ввели некорректное количество журавликов')
else:
    children_one_and_two = all_bird // 6
    children_three = children_one_and_two * 4
    print(F'Петя и сережа сделали по {children_one_and_two} журавликов, а Катя сделала {children_three} журавликов')



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


number_ticket = input('Введите шестизначный номер билета: ')
if len(number_ticket) != 6:
    print('Введите корректное значение')
else:
    digits = [int(digit) for digit in number_ticket]
    summ_first_half = sum(digits[:3])
    summ_second_half = sum(digits[3:])
    if summ_first_half == summ_second_half:
        print('Билет счастливый! Можно съесть!')
    else:
        print('Очень жаль =( Попробуй в следующий раз')



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите значение n: '))
m = int(input('Введите значение m: '))
k = int(input('Введите значение k: '))
if k <= n * m and (k % n == 0 or k % m == 0): ## или k < n * m, если один второй кусок не может быть равен 0
    print('yes')
else:
    print('no')

