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


def count_neighbors(table: list, row: int, col: int) -> int:  # подсчёт соседей клетки
    return sum([sum(table[row - 1 + i][col - 1:col + 2]) for i in range(3)]) - table[row][col]


def create_table(row: int, col: int) -> list:  # создаём двумерный сипсок больше ввёденного
    return [[0 for _ in range(col + 2)] for _ in range(row + 2)]


def print_table(table: list) -> None:  # Выводим поле в нужном формате
    for row in table[1:-1]:
        for elem in row[1:-1]:
            if elem == 1:
                print('X', end='')
            else:
                print('.', end='')
        print()


def next_state(table: list, row: int, col: int) -> list:  # создаём следующее состояние
    next_table = create_table(row, col)
    for x in range(1, row + 1):
        for y in range(1, col + 1):
            neighbors = count_neighbors(table, x, y)
            if table[x][y] == 1 and 2 <= neighbors <= 3:
                next_table[x][y] = 1
            elif table[x][y] == 0 and neighbors == 3:
                next_table[x][y] = 1
            else:
                next_table[x][y] = 0
    return next_table


def rect_to_tore(table: list) -> list:
    # Костыль превращающий прямоугольное поле в тор, даёт неправельные результаты при размерах поля < 3

    for i in range(1, len(table) + 1):
        table[i][0] = table[i][-2]
        table[i][-1] = table[i][1]
    table[0] = table[-2].copy()
    table[-1] = table[1].copy()
    table[0][0] = table[-2][-2]
    table[-1][0] = table[1][-2]
    table[-1][-1] = table[1][1]
    table[0][-1] = table[-2][1]
    return table


if __name__ == '__main__':
    row, col = map(int, input().split())
    table = create_table(row, col)
    for i in range(1, row + 1):
        table[i] = [0, *list(map(lambda s: int(s == 'X'), input().split())), 0]
    print_table(next_state(rect_to_tore(table), row, col))
