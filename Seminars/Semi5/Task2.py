# 33. Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# [1, 1, 1, 3, 2, 5, 5] -> [1, 1, 1, 3, 2, 1, 1]
# [2, 3, 4, 10 , 10, 2] -> [2, 3, 4, 2 , 2, 2]

my_list = list(map(int, input().split()))
low = min(my_list)
high = max(my_list)
for i in range(len(my_list)):
    if my_list[i] == high:
        my_list[i] = low
print(my_list)

# Второй вариант:


def change_grades(my_list):
    low = min(my_list)
    high = max(my_list)
    for i in range(len(my_list)):
        if my_list[i] == high:
            my_list[i] = low
    return my_list


print(change_grades(list(map(int, input().split()))))
