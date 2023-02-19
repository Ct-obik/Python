# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

def check():
    is_correct = True
    while is_correct:
        a = input()
        try:
            a = int(a)
            is_correct = False
            return a
        except ValueError:
            print('Некорректный ввод. Введите заново.')
print('Введи n:')
n = check()
print('Введи m:')
m = check()
print('Введи k:')
k = check()
print(n,m,k)
if (k % n == 0 or k % m == 0) and (k>=m and k>=n): print('yes')
else: print('no')