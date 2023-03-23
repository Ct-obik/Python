# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

#  a - открытие для добавления данных, дописывать, если файла нет - создаст и запись
#  r - открытие для чтения данных, если файла нет - ошибка
#  w - открытие для записи данных, если нет файла - создаст
#  w+ - запись, чтение, создание
#  r+ - чтение, дописывать, если файла нет - ошибка

# python Task1.py


def show_data() -> str:
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    print(book)


def new_data() -> str:
    with open('data.txt', 'a', encoding='utf-8') as file:
        fio = input('Введите ФИО: ')
        phone = input('Введите ')
        file.write(f'{fio} | {phone}\n')


def find_data() -> str:
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        temp = input('Веедите запрос: ')
        result = [(data.index(book), book)
                  for book in data if temp in book]
        if len(result) >= 1:
            [print(f'{result.index(book)+1}) {str(book[1])}')
             for book in result]
            return ([line[0] for line in result], data)
        else:
            return ([], data)


def rewrite_data(strings, data) -> str:
    fio = input('Введите новые ФИО: ')
    phone = input('Введите новый телефон: ')
    with open('data.txt', 'w', encoding='utf-8') as file:
        [file.write(f'{fio} | {phone}\n') if line == strings else file.write(
            f'{data[line]}\n') for line in range(len(data)-1)]


def edit_data() -> str:
    data = find_data()
    if len(data[0]) == 1:
        rewrite_data(data[0][0], data[1])
    elif len(data[0]) > 1:
        change = int(input('Введи номер для изменения: '))
        while change not in [i for i in range(1, len(data[0])+1)]:
            print('Не верный номер')
            change = int(input('Введи номер для изменения: '))
        rewrite_data(int(data[0][change-1]), data[1], data.txt)


def del_data(strings, data):
    with open('data.txt', 'w', encoding='utf-8') as file:
        [file.write(f'{data[line]}\n') if line !=
         strings else '' for line in range(len(data)-1)]
        print('Запись удалена')


def delete_data():
    data = find_data()
    if len(data[0]) == 1:
        del_data(data[0][0], data[1])
    elif len(data[0]) > 1:
        change = int(input('Введи номер для изменения: '))
        while change not in [i for i in range(1, len(data[0])+1)]:
            print('Не верный номер')
            change = int(input('Введи номер для изменения: '))
        del_data(int(data[0][change-1]), data[1], data.txt)


while True:
    mode = input('Выберите режим работы справочника:\
                \n 1. Показать содержимое справочника\
                \n 2. Добавить новую информацию в справочник\
                \n 3. Найти нужную информацию в справочнике\
                \n 4. Изменение информации\
                \n 5. Уадаление нужной информации\
                \n 0. Выйти из программы\
                 \n')
    if mode == '1':
        show_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        find_data()
    elif mode == '4':
        edit_data()
    elif mode == '5':
        delete_data()
    elif mode == '0':
        break
    else:
        print('No mode')
