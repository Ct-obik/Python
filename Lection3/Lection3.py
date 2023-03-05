"""Функция - фрагмент кода, который можно использовать нмогократно (DEF)"""


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)        # return summa - возвращает summa и завершает работу функции


sum_numbers(5)


def sum_str(*args):     # Спомощью * можем передавать неограниченное кол-во аргументов
    res = ''
    for i in args:
        res += i
    return res


print(sum_str('q', 'e', 'r'))
print(sum_str('q', 'e', 'r', 't', 'y'))
# print(sum_str(1,8,9))      # Чтобы работать с int, надо res = 0

"""
Модуль - это фалй, в котором прописаны функции
"""
import modul1
print(modul1.max1(5, 9))
from modul1 import max1     # Импортируем только определённую функцию. Если указать * вместо max1, то импортируем все функции
print(max1(8, 1))
import modul1 as m1         # Можно переименовать модуль для удобства
print(m1.max1(2, 4))

"""
Рекурсия - функция, вызывающая сама себя
"""
# Фибоначчи
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n -2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

"""
Алгортимы
"""
# Быстрая сортировка
print('Быстрая сортировка:')
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([14,5,5,8,9,7,6,3,10,12,5,25]))

# Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)