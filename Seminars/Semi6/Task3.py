# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные друг другу
# образуют одну пару, которую необходимо посчитать. Вводится список чисел
# через пробел в одну строку. (сочетания без повторений)
# [2, 2, 2, 2] -> 6

def get_count_pairs_2(user_list: list):
    count_pairs = 0
    for i in range(len(user_list)):
        count_pairs += user_list[i + 1:].count(user_list[i])
    return count_pairs


arr = [1, 2, 1, 2, 1, 2, 2]
print(get_count_pairs_2(arr))