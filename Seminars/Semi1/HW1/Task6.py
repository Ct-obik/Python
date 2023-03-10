# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
print('Введи номер билета:')
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
i = a // 100000 + (a // 10000) % 10 + (a // 1000) % 10
j = a % 10 + (a % 100) // 10 + (a % 1000) // 100
if i==j:
    print('ПОЗДРАВЛЯЕМ! У вас счастливый билет. Созраните его в кошельке и всегда носите с собой :)')
else: print('Пожалуйста, сохраняйте билет до окончания поездки')