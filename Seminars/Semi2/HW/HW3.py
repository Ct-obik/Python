# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2**k), не превосходящие числа N.

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

print('Введите число N:')
N = check()
n = 0
count = -1
while N > n:
    n = 2 ** (count + 1)
    count += 1
    if N > n:
        print(n, end=" ")
