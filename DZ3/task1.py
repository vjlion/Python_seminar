# Задача 16: Требуется вычислить, 
# сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой 
# строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 3
#  -> 1
from random import randint
n = int (input("Введите количество элементов "))
x = int (input("Введите число X: "))
list_1 = [randint(1, 10) for _ in range(n)]
count = 0
for i in range(n):
    if list_1[i] == x:
        count += 1
print(list_1)
print(f'Число {x} встречается в списке {count} раз') 



