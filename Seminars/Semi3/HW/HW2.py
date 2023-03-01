# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n)
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
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
    n = randint(0, 100)     # Делаем рандом от 0 до 100
    list_1.insert(0, n)
print(list_1)
print('Введите искомое число:')
num_x = check()
num_near = 0
min = abs(list_1[0] - num_x)
for i in range(len(list_1) - 1):
    if (abs(list_1[i] - num_x) <= min):
        min = abs(list_1[i] - num_x)
        num_near = list_1[i]
print(f'Самый близкий по величине = {num_near}')
