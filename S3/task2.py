# Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint
n = int (input("Введите количество элементов "))
K = int (input("Введите число K "))
list_1 = [randint(1, 10) for _ in range(n)]
print(list_1)
j = -1
for i in range(K, n):
    j += 1
    list_1.insert(j, list_1[i])
    list_1.pop(i + 1)
print(list_1)

# numbers = [1, 2, 3, 4, 5]
# k = int(input()) % len(numbers)
# for i in range(k-1):
#     numbers.insert(0, numbers.pop())
# print(numbers)