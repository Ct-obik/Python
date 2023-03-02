# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит
# в последовательность)”. Однако 2 друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.

# Ваня
n = int(input())
max_num = 1000          # max_num = n
while n != 0:
    n = int(input())
    if max_num > n:    # max_num < n
        max_num = n
print(max_num)
# Петя
n = int(input())
max_num = -1            # max_num = n
while n < 0:            # while n != 0
    n = int(input())
    if max_num < n:
        n = max_num     # max_num = n
print(n)                # print(max_num)

# Идеальное решение, а победил Ваня.
n = int(input())
max_num = n
while n != 0:
    n = int(input())
    if max_num < n:
        max_num = n
print(max_num)
