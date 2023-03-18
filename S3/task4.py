# Задача №23. 
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint
n = int (input("Введите количество элементов "))
counter = 0
list_1 = [randint(1, 10) for _ in range(n)]
print(list_1)
for i in range(1, n):
    if list_1[i-1] < list_1[i]:
        counter += 1
print(counter)