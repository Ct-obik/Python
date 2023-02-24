# 9 По данному целому неотрицательному n вычислите значение n!.
# N1 = 1 * 2 * 3 * ... * N

n = int(input())
fact = 1
if n == 0:
    print(1)
else:
    while n > 1:
        fact *= n   # fact = fact * n
        n -= 1      # n = n - 1
    print(fact)
