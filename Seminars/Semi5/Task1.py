# '31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# n = int(input())
def find_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n_0 = 0
        n_1 = 1
        for i in range(n-2):
            # temp = n_0
            # n_0 = n_1
            # n_1 = temp + n_0  можно сократить:
            n_0, n_1 = n_1, n_0 + n_1
            result = n_0 + n_1
    return result


print(find_fibonacci(int(input())))

# Второе решение:


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


print(fibonacci(int(input())))
