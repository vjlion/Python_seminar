# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2
from random import randint
n = int(input('Введите количество монеток: '))
count_zero = 0
count_one = 0
for i in range(n):
    x = randint(0, 1)
    print(x)
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
print()
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
