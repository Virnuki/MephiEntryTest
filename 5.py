"""
Задача 5
 Напишите программу, которая получает на вход пять карт и выводит старшую
 покерную комбинацию, которая образуется этими картами.
 На ввод подаётся одна строка, в которой указаны пять карт в формате <value><suit>,
 записанные через пробел. На вывод должно пойти название старшей комбинации,
 сформировавшейся на пришедшем наборе.
 Справочные данные:
 Value: [2 3 4 5 6 7 8 9 10 J Q K A]
 Suit: [D H S C]
 Комбинации в порядке ослабления:
 Флеш-рояль: состоит из 5 старших карт одной масти, начинающихся с туза,
 например: Т♥ К♥ Д♥ В♥ 10♥
 Стрит-флеш: любые пять карт одной масти по порядку, например: 9♠ 8♠ 7♠ 6♠ 5♠.
 Каре: четыре карты одного достоинства, например: 3♥ 3♦ 3♣ 3♠.
 Фулл-хаус: один сет и одна пара, например: 10♥ 10♦ 10♠ 8♣ 8♥.
 Флеш: пять карт одной масти, например: К♠ В♠ 8♠ 4♠ 3♠.
 Стрит: пять карт по порядку любых мастей, например: 5♦ 4♥ 3♠ 2♦ Т♦.
 Сет: три карты одного достоинства, например: 7♣ 7♥ 7♠.
 Две пары: две пары карт, например: 8♣ 8♠ 4♥ 4♣.
 Одна пара: две карты одного достоинства, например: 9♥ 9♠.
 Старшая карта: ни одна из вышеописанных комбинаций

 A D Q D K D J D 10 D
 Флеш-рояль
 4 S 2 S 5 S A S 3 S
 Стрит-флеш
 8 D 8 H A H 8 C 8 S
 Каре
 10 C 8 S 8 C 10 H 10 D
 Фулл-хаус
 K D J D 3 D 8 D 4 D
 Флеш
 5 S 8 C 6 S 7 D 4 D
 Стрит
 7 D 7 S 3 S 8 D 7 H
 Сет
 8 D 4 C 4 S 7 H 8 S
 Две пары
 9 D 9 S 2 C 5 H Q S
 Одна пара
 2 D 6 C 9 H A S J S
 Старшая карта
"""


VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7': 7, '8': 8, '9': 9,
              '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}  # Словарь для преобразования значения в число


def input_cards(s: str) -> list:  # Преобразование строки в удобный вид
    s = s.split()
    out = []
    for i in range(0, len(s), 2):
        out.append([VALUES[s[i]], s[i + 1]])
    return out


def flush(cards: list) -> bool:  # Проверка на флеш
    if [card[1] for card in cards].count(cards[0][1]) == len(cards):
        return True
    return False


def street(cards: list) -> bool:  # Проверка на стрит
    vals = [card[0] for card in cards]
    vals.sort()
    for i in range(len(vals) - 1):
        if not (vals[i] + 1 == vals[i + 1] or (vals[i] == 5 and vals[i + 1] == 14)):
            return False
    return True


def count_repeats(cards: list) -> list:  # Подсчёт карт с одинаковым номиналом
    vals = [card[0] for card in cards]
    return [vals.count(vals[i]) for i in range(len(vals))]


def find_combinations(cards: list) -> None:  # Ищем страшную комбинацию и выводим
    is_flush = flush(cards)
    is_street = street(cards)
    repeats = count_repeats(cards)
    cards.sort()
    if is_flush and is_street and cards[-2][0] == 13:
        print('Флеш-рояль')
    elif is_flush and is_street:
        print('Стрит-флеш')
    elif 4 in repeats:
        print('Каре')
    elif repeats.count(3) == 3 and repeats.count(2) == 2:
        print('Фулл-хаус')
    elif is_flush:
        print('Флеш')
    elif is_street:
        print('Стрит')
    elif 3 in repeats:
        print('Сет')
    elif repeats.count(2) == 4:
        print('Две пары')
    elif 2 in repeats:
        print('Одна пара')
    else:
        print('Старшая карта')


if __name__ == '__main__':
    find_combinations(input_cards(input()))