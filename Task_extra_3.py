# 5. Сумма дробей (часть первая)
# Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).

# # Ввод:
# >> 5
# # Вывод:
# >> 7.5

summ = 1
n = int(input('Введите число N: '))
for i in range(1, n+1):
    summ += 1 + i/10
print(f'Искомая сумма равна: {summ}')
