"""
Задача 6
 Выведите таблицу размером n×n, заполненную целыми числами от 1 до n^2 по
 спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке.
 Пример:
 5
 Вывод:
 1   2   3   4   5
 16 17 18 19 6
 15 24 25 20 7
 14 23 22 21 8
 13 12 11 10 9
"""

n = int(input())  # Ввод
table = [[i for i in range(1, n + 1)] for j in range(n)]  # Заготавливаем список
direction = 1
cycle = 1
step = 1
sub_step = 0
count = n
while count < n * n:  # Основной цикл
    for i in range(n - step):  # Заметим, что спираль можно построить из прямоугольников парами одного размера
        count += 1
        if direction == 1:  # Движемся вниз
            table[cycle + i][-1 * cycle] = count
        elif direction == 2:  # Влево
            table[-1 * cycle][n - i - cycle - 1] = count
        elif direction == 3:  # Вверх
            table[-1 - cycle - i][cycle - 1] = count
        else:  # Вниз
            table[cycle][cycle + i] = count
    if direction == 0:  # Меняем отступ
        cycle += 1
    direction = (direction + 1) % 4  # Меняем направление
    sub_step = (sub_step + 1) % 2  # Меняем размер прямоугольника
    if sub_step == 0:
        step += 1

for row in table:  # Вывод
    for elem in row:
        print(elem, end=' ')
    print()