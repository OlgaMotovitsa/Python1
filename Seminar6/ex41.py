# Задача №41. Решение в группах
# Дан список, состоящий из целых чисел. Напишите
# программу, которая в данном списке определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:             Ввод:
# 5                 5
# 1 2 3 4 5         1 5 1 5 1
# Вывод:            Вывод:
# 0                 2
# (каждое число вводится с новой строки)

import random

# list_1 = [random.randint(1, 10) for _ in range(int(input("Введите количество элементов в списке 1: ")))]
# print(list_1)


# count = 0
# for i in range(1, len(list_1)-1): # в списке рандомных чисел от 1го элемента до элемента длина списка - 1(последрний элемент)
#     if list_1[i] > list_1[i-1] and list_1[i+1]:
#     # if list_1[i-1] < list_1[i] > list_1[i+1]:
#         count +=1
# print(count)

my_list = [random.randint(0, 10) for _ in range(10)]
print(my_list)


for i in range (12):   # зациклили и 12 раз будем рассматривать по очереди значения
    print(my_list[(i-1) % len(my_list)], my_list[(i) % len(my_list)], my_list[(i+1) % len(my_list)] )