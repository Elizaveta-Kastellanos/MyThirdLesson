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

try:
    num = int(input('Введите десятичное число: '))
    num2 = ''
    while num > 0:
        num2 = str(num % 2) + num2
        num //= 2
    print(num2)
except ValueError:
    print('Упс! Что-то пошло не так, попробуй ввести число!')

# 5.) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:  - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

try:
    mas = []
    f0, f1 = 1, 1
    while True:
       n = int(input('Введите число N: '))
       if n > 2 and n < 20:
        break
    nn = -n
    i = 1
    f_1 = f1 - f0
    while i >= nn:
        f0, f1 = f1 - f0, f0
        mas.append(f1)
        i = i - 1
    mas.reverse()
    mas.append(1)
    f0, f1 = 1, 1
    for i in range(2, n):
         f0, f1 = f1, f0 + f1
         mas.append(f1)
    print(*mas)
except ValueError:
    print('Упс! Что-то пошло не так, попробуй ввести число!')
