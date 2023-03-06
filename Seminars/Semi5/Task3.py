# 35. 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

def prime_number(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


print(prime_number(int(input("Введите число: "))))