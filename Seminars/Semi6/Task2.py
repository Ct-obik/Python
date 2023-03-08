# Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов, у которых два соседних и,
# при этом, оба соседних элемента меньше данного. Элементы массива вводятся
# на одной строке через пробел. Массив состоит из целых чисел. Список не циклический
# [1, 2, 1, 3, 4, 3] -> 2 (2, 4)

def get_list(count: int) -> list[int]:
    new_list = list()
    for i in range(count):
        new_list.append(int(input(f'Введите {i + 1}-й элемент: ')))
    return new_list


def get_count_max_element(first_list: list[int]) -> int:
    if len(first_list) < 3:
        return 0
    count = 0
    for i in range(1, len(first_list) - 1):
        if first_list[i-1] < first_list[i] > first_list[i+1]:
            count += 1
    return count


first_list = list(map(int, input('Введите массив: ').split()))
print(get_count_max_element(first_list))