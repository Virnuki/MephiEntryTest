"""
 Задача 2
 Напишите программу, которая принимает с клавиатуры координаты шахматного
 ферзя и отрисовывает доску следующим образом:
 буквой Q обозначается положение фигуры;
 клетки, по которым может ударить ферзь, обозначены «*»;
 остальные клетки обозначены «.»
 Пример:
 Enter cell to place queen:
 >> c4
 Chess board:
 . . * . . . * .
 . . * . . * . .
 * . * . * . . .
 . * * * . . . .
 * * Q * * * * *
 . * * * . . . .
 * . * . * . . .
 . . * . . * . .
"""


def letter_to_index(s: str) -> int:
    # Переводим название столбца в его индекс в списке при помощи разницы в номере кодировки UTF-8
    if s not in 'abcdefgh':  # Проверяем есть ли столбец на доске
        raise ValueError(f'Letter {s} not on chess board')
    return ord(s) - ord('a')


def create_table() -> list:  # Создаём доску как список списков
    table = [['. '] * 8 for _ in range(8)]
    return table


def print_table(table: list) -> None:  # Выводим игральную доску
    for row in table:
        print(''.join(row).rstrip())


def place_queen(s: str, table: list) -> list:  # Ставим ферзя на доску и отмечаем клетки под боем
    x, y = 8 - int(s[1]), letter_to_index(s[0])  # Переводим ввёденное название клетки в координаты
    if not 1 <= x <= 8:  # Проверяем есть ли такая строка на доске
        raise ValueError(f'Number {s[1]} not on chess board')
    for i in range(8):  # Отмечаем клетки под боем
        for j in range(8):
            if i == x or j == y or x - y == i - j or x + y == i + j:
                # Та же строка, тот же столбец, диагональ право-низ, диагональ право-верх
                table[i][j] = '* '
    table[x][y] = 'Q '  # Ставим ферзя
    return table


if __name__ == '__main__':
    print_table(place_queen(input('Enter cell to place queen:\n'), create_table()))
