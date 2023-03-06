# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму
# двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
#     4

def sum(a, b):
    if b != 0:
        b -= 1
        a += 1
        sum(a, b)
    else:
        print(a)


a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
print('Сумма равна = ', end='')
sum(a, b)

# PS Смысл решения:
# мы вычитаем из одного числа и прибавляем к другому.
# Дойдя до 0, мы все числа и просуммируем!
