"""
Задача 3
 Напишите программу, вычисляющую следующее состояние поля для игры «Жизнь»
 (https://ru.wikipedia.org/wiki/Игра_«Жизнь»).
 Поле представляет собой тор (т.е. замкнутый прямоугольник, для крайних клеток
 которого соседними являются клетки с противоположного конца; каждая клетка
 всегда имеет 8 соседей).
Формат ввода: на первой строке указаны два целых числа через пробел: высота и
 ширина поля. В следующих строках подаётся состояние поля. Символ "." обозначает
 мёртвую клетку, "X" − живую.
 Формат вывода: следующее состояние поля, используя те же обозначения, что
 использовались на вводе.
 Пример:
 5 6
 .  .  .  X  X  .
 .  X  X  .  .  .
 .  .  X  .  .  .
 X  X  .  .  .  .
 X  .  .  X  X  .
 Вывод:
 .X..XX
 .XX...
 X.X...
 XXXX.X
 XXXXX.
"""


def count_neighbors(table: list, row: int, col: int, l_y: int, l_x: int) -> int:  # подсчёт соседей клетки
    count = table[row][col] * -1
    for i in range(3):
        for j in range(3):
            count += table[(row - 1 + i) % l_y][(col - 1 + j) % l_x]
    return count


def create_table(row: int, col: int) -> list:  # создаём двумерный сипсок больше ввёденного
    return [[0 for _ in range(col)] for _ in range(row)]


def print_table(table: list) -> None:  # Выводим поле в нужном формате
    for row in table:
        for elem in row:
            if elem == 1:
                print('X', end='')
            else:
                print('.', end='')
        print()


def next_state(table: list, row: int, col: int) -> list:  # создаём следующее состояние
    next_table = create_table(row, col)
    for x in range(row):
        for y in range(col):
            neighbors = count_neighbors(table, x, y, row, col)
            print(neighbors)
            if table[x][y] == 1 and 2 <= neighbors <= 3:
                next_table[x][y] = 1
            elif table[x][y] == 0 and neighbors == 3:
                next_table[x][y] = 1
            else:
                next_table[x][y] = 0
    return next_table


if __name__ == '__main__':
    row, col = map(int, input().split())
    table = create_table(row, col)
    for i in range(row):
        table[i] = list(map(lambda s: int(s == 'X'), input().split()))
    print_table(next_state(table, row, col))
