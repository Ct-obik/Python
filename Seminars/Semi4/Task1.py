# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# a a a b c a a d c d d
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 

# def getStrWithCount(lst: list) -> str:
#     res_list, res_str = [], ""
#     for item in lst:
#         res_str += f"{item} " if item not in res_list else f"{item}_{res_list.count(item)} "
#         res_list.append(item)
#     return res_str.rstrip()


# lst = list(input("Введите список через пробел\n").split())
# print(getStrWithCount(lst))
"""Второй вариант решения задачи с помощью сдвига"""
symbols = input()
new_string = ''
sdvig = 0
for i in symbols.split():
    if symbols[0:sdvig].count(i) != 0:
        new_string += f'{i}_{symbols[0:sdvig].count(i)} '
    else:
        new_string += f'{i} '
    sdvig += 2
print(new_string)
