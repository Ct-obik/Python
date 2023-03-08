# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит первый массив через пробел и второй через пробел на разных строках.
# [1, 2, 3, 4, 5]
# [1, 2, 3] -> [4, 5]

def get_list(count: int) -> list[int]:
    new_list = list()
    for i in range(count):
        new_list.append(int(input(f'Введите {i + 1}-й элемент: ')))
    return new_list


def print_unique_element(first_list: list[int], second_list: list[int]):
    result = ''
    for item in first_list:
        if item not in second_list:
            result += f'{item} '
    print(result)


first_list = list(map(int, input('Введите первый массив: ').split()))
second_list = list(map(int, input('Введите второй массив: ').split()))
print_unique_element(first_list, second_list)
