# найти сумму чисел с ввода через рекурсию

def find_sum(n):
    if len(n):
        return n[0] + find_sum(n[1:])
    return 0


print(find_sum(list(map(int, input().split()))))
