# Задача 16: Требуется вычислить, сколько раз встречается
# некоторое число X в массиве из случайных чисел. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X
from random import randint
print('Введите кол-во элементов:')


def check():
    is_correct = True
    while is_correct:
        a = input()
        try:
            a = int(a)
            is_correct = False
            return a
        except ValueError:
            print('Некорректный ввод. Введите заново.')


num = check()
list_1 = []
for i in range(num):
    n = randint(0, 9)
    list_1.insert(0, n)
print(list_1)
print('Введите искомое число:')
num_x = check()
count = 0
i = 0
for i in range(len(list_1) - 1):
    if list_1[i] == num_x:
        count += 1
print(f'Ваше число {count} раз встречается в массиве')
