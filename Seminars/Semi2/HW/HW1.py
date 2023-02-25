# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
print('Сколько кидаем монет?')

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

n = check()
count_O = 0
count_I = 0
for i in range(n):
    monets = randint(0, 1)
    print(monets)
    if monets == 0:
        count_O += 1
    if monets == 1:
        count_I += 1
print(f'Кол-во монет с решкой (0) = {count_O}')
print(f'Кол-во монет с орлом (1) = {count_I}')
if count_O > count_I:
    print(f'Минимум надо перевернуть {count_I} с орлом')
else:
    print(f'Минимум надо перевернуть {count_O} с решкой')