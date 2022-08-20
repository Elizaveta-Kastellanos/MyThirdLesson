#1.) Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list_for_sum = [2, 3, 5, 9, 3] #[random.randint(-100, 100) for i in range(10)]
sum = 0
for i in range(len(my_list_for_sum)):
    if i % 2 != 0:
        sum += my_list_for_sum[i]
print(sum)


#2.) Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];  - [2, 3, 5, 6] => [12, 15]

my_list_for_mult = [2, 3, 4, 5, 6]
new_list_for_mult = []
for i in range(len(my_list_for_mult)//2):
    if len(my_list_for_mult) % 2 != 0:
       new_list_for_mult.append(my_list_for_mult[i] * my_list_for_mult[len(my_list_for_mult)-i-1])
       if i == len(my_list_for_mult)//2 - 1:
        new_list_for_mult.append(my_list_for_mult[len(my_list_for_mult)//2] * my_list_for_mult[len(my_list_for_mult)//2])
    else:
        new_list_for_mult.append(my_list_for_mult[i] * my_list_for_mult[len(my_list_for_mult)-i-1])
print(new_list_for_mult)

print('-------------------')

#3.) Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
 
my_list_for_max_and_min = [1.1, 1.2, 3.1, 5, 10.01]
min_num = my_list_for_max_and_min[0] - int(my_list_for_max_and_min[0])
max_num = my_list_for_max_and_min[0] - int(my_list_for_max_and_min[0])
for i in range(1, len(my_list_for_max_and_min)):
    tmp = my_list_for_max_and_min[i] - int(my_list_for_max_and_min[i])
    if tmp < min_num:
        min_num = tmp
    if tmp > max_num:
        max_num = tmp
print(round(max_num-min_num, 20))



# 4.) Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101;  - 3 -> 11;  - 2 -> 10    


# 5.) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:  - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]
# (https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%
# D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:
# text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B
# 5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%
# B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%
# D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B
# 5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0
# %BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%
# D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87
# %D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)    


