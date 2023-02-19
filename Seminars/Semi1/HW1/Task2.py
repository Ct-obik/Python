#   Найдите сумму цифр трехзначного числа.

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


a = check()
if 99 < a < 1000:
    print(a % 10 + a // 100 + a % 100 // 10)
else:
    print('Введите другое число')
