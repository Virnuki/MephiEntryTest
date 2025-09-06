"""
Задача 1
 Напишите программу, которая создаёт список списков, элементами которого
 являются все возможные подсписки исходного списка, включая пустой.
 На вход программы подаётся несколько букв, из которых формируется список.
 Пример:
 Please, enter some letters to covert to list:
 >> a b c
 Sub-lists are:
 [[], [a], [b], [c], [a, b], [b, c], [a, b, c]]
"""

input_list = input("Enter some letters to covert to list:\n").split()  # Ввод строки и разбиение на список
out_list = [[]]
for i in range(len(input_list)):  # Берём индекс начала среза
    for j in range(i, len(input_list)):  # Берём индекс концасреза
        out_list.append(input_list[i:j + 1])  # Добавляем наш срез в конец списка
out_list.sort(key=len)  # Сортируем список по длине среза
print("Sub-lists are:", out_list, sep="\n")  # Выводим в нужном формате
