# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X


x = int(input())
array = []
for i in range(1, x+1):
    array.append(i)
    print(array[i-1], end = ' ')
print()
y = int(input())
if y >= array[x-1]:
    print(array[x-1])
elif y <= array[0]:
    print(array[0])
else:
    print(y)