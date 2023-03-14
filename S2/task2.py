# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input('Введите чило: '))
count = 2
n1 = 0
n2 = 1
key = True
while key:
    nf = n1+n2
    if nf < n:
        n1 = n2
        n2 = nf
        count += 1
    elif nf == n:
        count += 1
        key = False
    else:
        count = -1
        key = False
print(count)
