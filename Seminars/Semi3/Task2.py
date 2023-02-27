# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число. 1 2 3 4 5 K = 3 -> 3 4 5 1 2

from random import randint
n = int(input())
k = int(input())
list_ = []
list_ = [i for i in range(n)]
print(list_)
for i in range(k):
    temp = list_.pop()
    list_.insert(0, temp)
print(list_)

# # Второй вариант
# n = int(input())
# k = int(input())
# result = [i for i in range(n)]
# for i in range(k):              сдвиг влево
#     result.append(result.pop(0))
# print(result)

# for i in range(k):              сдвиг вправо
#     result.insert(0, result.pop())
# print(result)