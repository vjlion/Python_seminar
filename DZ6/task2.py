# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
my_array = int(input("введите количество массива: "))
list_1 = list(random.randint(-10, 10) for i in range(my_array))
print(list_1)
min_number = int(input('Введите min -> '))
max_number = int(input('Введите max -> '))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end=" ")
