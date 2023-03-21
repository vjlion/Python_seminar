# Задача №29. «На вход программе подаются цифры,
# как только пользователь введёт 0 ввод прекращается.
# Вывести наибольший элемент получившейся последовательности».
# Есть два кода с ошибками, нужно определить где ошибок меньше.

# Примечание: Программные коды на следующих слайдах

# # Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)

# # Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)

n = int(input())
max_number = -1
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)