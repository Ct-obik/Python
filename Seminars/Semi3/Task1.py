# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# 1 2 3 1 2 4 -> 4 (1 2 3 4)

list_ = []
n = 6
for i in range(n):
    list_.append(int(input()))
print()
print(len(set(list_)))
