# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в порядке 
# возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

set_1 = []
N = int(input("Введите количество элементов в 1м массиве  "))
for i in range (N):
    set_1 = [random.randint(0,10) for i in range(int(N))]
    
print(set_1)
print(set(set_1))

set_2 = []
N = int(input("Введите количество элементов в 1м массиве  "))
for i in range (N):
    set_2 = [random.randint(0,10) for i in range(int(N))]
    
print(set_2)
print(set(set_2))

set_3 = set(set_1).intersection(set_2)
print(f'Oдинаковые значения в 2х множествах в порядке возрастания', (set_3))






# set_3 = set_1 + set_2


# similar_nums_list = []
# result = []
# for i in set_3:
#     if set_3.count(i) > 1 and i not in similar_nums_list:
#         similar_nums_list.append(i)
#         result.append(i)
# print("одинаковые значения в 2х множествах в порядке возрастания",result)