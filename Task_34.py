'''
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
'''

def song_true(song_str):
    vowel_letters = 'аяуюоеёэиы'
    count = 0
    for i in song_str:
        if i in vowel_letters:
            count += 1
    return count

song = input('Винни, введи текст своей песни: ').split()
song_str_vowel = set(map(song_true, song))

if len(song_str_vowel) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
