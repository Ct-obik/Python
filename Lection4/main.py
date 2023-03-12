"""Работа с ссылками. Ссылки - это когда мы используем, например, название функции
в другой функции для связи данных"""
# Пример 1
def f(x):
    return x*x


a = f
print(f(5))
print(a(5))

# Пример 2
def calk1(a):
    return a+a


def calk2(a):
    return a*a


def math(op, x):
    print(op(x))


math(calk1, 5)
math(calk2, 10)

# Пример 3
def calk1(a, b):
    return a+b


def calk2(a, b):
    return a*b


def math(op, x, y):
    print(op(x, y))


math(calk1, 5, 45)
math(calk2, 10, 5)

"""
Лябда-функция 
lambda
"""
print('Work with Lambda')
def calk2(a, b):
    return a*b


def math(op, x, y):
    print(op(x, y))

calk1 = lambda a, b: a + b  # Можно преобразовать
                            # в одну строку
math(calk1, 10, 45)         # math(lambda a, b: a + b, 10, 45)

# Задача
# В списке числа. Найти четные и их квадрат.
# Первое решение
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i%2 == 0:
        res.append((i, i**2))
print(res)
# Второе решение, с помощью лямбды
def select(f, col):             # возвращает список, в котором мы к каждому эл-у применили функцию f
    return [f(x) for x in col]

def where(f,col):               # возвращает только те значения, которые прошли проверку условия f(x)
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res) # Выводим обычный список
res = where(lambda x: x % 2 == 0, res)
print(res) # Выводим чётные значения
res = list(select(lambda x: (x, x**2), res))
print(res) # Выводим  чётные значения с их квадратами
"""
MAP - принимает на вход 2 рагумента: функцию и объект
"""
list_1 = [x for x in range(1, 20)]
print(list_1)
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

# Задача: С клавиатуры вводим набор с пробелом. Превратить строки в числа
data = '15 156 96 3 5 8 52 5'
print(data)
# data = data.split()     # Нашу строку преобразовываем в список строк
# print(data)
data = list(map(int, data.split()))     # Преобразовываем в список чисел
print(data)

#Решение задачи: упрощаем с помощью функцей map
def where(f,col):
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res) 
res = list(map(lambda x: (x, x**2), res))
print(res)

""" Функция фильтр. Принимает на вход саму функцию и объект, и будет передавать только те значения, 
для которых вызов функции возвращает значение true"""
data = [16, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

#Решение задачи: упрощаем с помощью функцей map и функцией filter)
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
"""Функия zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами 
из элементов входных данных.
Функция zip() пробегает только по минимальному входящему набору данных"""
# Пример 
# zip ([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't'])
# [(1,'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
"""Функция enumerate применяется к итерируемому объекту и возвращает
новый итератор с кортежами из индекса и элементов входных данных.
Позволяет пронумировать набор данных.
"""
# Пример:
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

 """Ф А Й Л Ы"""
# Файлы в текстовом формате используются для:
# - хранения данных
# - передачи данных в клиент-серверных проектах
# - хранения конфигов
# - логирования действий
# Что нужно для работы с файлами:
# 1 - завести переменную, которая будет связана с этим текстовым файлом
# 2 - указать путь к файлу
# 3 - указать, в каком режиме мы будем работать с файлом
# Режимы:
#  a - открытие для добавления данных, дописывать, если файла нет - создаст и запись
#  r - открытие для чтения данных, если файла нет - ошибка
#  w - открытие для записи данных, если нет файла - создаст
#  w+ - запись, чтение, создание
#  r+ - чтение, дописывать, если файла нет - ошибка

#///////    примеры работы с файлами:       //////
#       Режим добавления
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')    указываем режим работы, в котором будем работать
# data.writelines(colors)
# data.close()

#       режим записи
# with open('file.txt', 'w') as data:
#     data.writa('line 1\n')
#     data.write('line 2\n')
# print(56)

#       режим чтения
# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

"""Модуль OS
Множество функций для работы с ОС. Необходимо его импортировать в свойю программу: import os"""
# Базовые функции:
# os.chdir(path) - смена текующей директории:
#     import os
#     os.chdir('C:/User/GB/')
# os.getcwd() - текущая рабочая директория
#     import os
#     print(os.getcwd())
# os.path - множество ещё функций
# print(os.path.basename('ПУТЬ')) - базовое имя пути
# print(os.path.abspath('main.py')) - возвращает нормализованный абсолютный путь
"""Модуль Shutil
Содержит набор функций высокого уровня для обработки файлов, групп файлов и папок.
Позволяют копировать, перемещать и удалять файлы и папки. Также импортироуем: import shutil
"""
#       Базовые функции:
# shutil.copyfile(src, dst) - копирует содержимое (не метаданные) файла src в файд dst
# shutil.copy(src, dst)   -   копирует содержимое файла src в файл или папку dst
# shutil.rmtree(path) - удаляет текущую директорию и все поддиректории; path должен указывать на директорию (не ссылку)