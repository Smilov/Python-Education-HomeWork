# 6.Даны положительные числа A, B, C. На прямоугольнике размера A x B размещено максимально возможное
# количество квадратов со стороной C (без наложений).
# Найти количество квадратов, размещенных на прямоугольнике. Операции умножения и деления не использовать.


a = int(input('Введите длину стороны А: '))
b = int(input('Введите длину стороны B: '))
c = int(input('Введите длину стороны C: '))
count_a = 0
count_b = 0
c_plus = c
square = 0
while c_plus <= a:
    count_a += 1
    c_plus += c
c_plus = c
while c_plus <= b:
    count_b += 1
    c_plus += c
for i in range(min(count_a, count_b)):
    square += max(count_a, count_b)
print(F'Количство квадратов: {square}')