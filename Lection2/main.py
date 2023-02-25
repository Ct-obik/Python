"""
        Списки
Список - это упорядоченный конечный набор элементов, тот же массив.
"""
# list_1 - []     Создание пустого списка
# list_2 - list() Создание пустого списка
# list_1 = [7, 8, 23, 15]   Создание списка
# print(*list_1)              вывод списка без скобок и запятых

# for i on list_1:      Вывод каждого элемента из списка
#     print(i)

# print(len(list_1))    вывод общего числа элементов в списке

# print(list_1[0])      вывод эл-а из списка

# list_1.append(8)    добавить в список в конец элемент = 8

# a = list_1.pop        pop возвращает элемент и
# print(a)              удаляет
# print(list_1.pop())   вывод списка с удалением последнего эл-а (в скобках можно указать индекс элемента)

# print(list_1.insert(2,11) добавление элемента на нужную позицию (1 - индекс, 2 - значение элемента)

"""
        Кортеж
 Это неизменный список. Защищает данные от изменений( намеренных или случ-ых).
 Занимает меньше места в памяти и работают быстрее, по сравнению со списками.
 Можем выводить, получать, как-то работать с ними
"""
# t = ()    создание пустого кортежа
# print(type(t))    class <'tuple'>
# t = (1, )         если не поставить запятую в конце, то класс кортеж изменится на другой
# print(type(t))    

# v = [1, 4, 7]     создаём список
# v = tuple(v)      сохраняем его (превращаем в кортеж)
# print(v)          выводим наш кортеж

# a,b,c = v         
# print(a, b, c)    выводим все элменты кортежа в отдельные элементы (распаковка кортежа)

# for i in t:       вывод всех элементов кортежа через цикл
#   print(i)

# for i in range(len(t)):   так же выводим
#   print(t[i])

"""
        Словари
Неупорядочные коллекции произвольных объектов с доступом по ключу.
В списках в качестве ключа используется индекс элемента. В словаре для определения
элемента используется значение ключа (строка, число)
"""
# d = {}        создание словаря
# d = dict()

# d['q'] = 'qwert'  до,авить значения в словарь
# d['w'] = 'werty'
# print(d['q'])     выводим значение по букве 'q'

# del dictionary['w']   удаление элемента из словаря

# dictionary = {'q': 'qwerty', 'w': 'werty'}
# for item in dictionary:                                   вывод полностью словаря
#     print('{}: {}'.format(item, dictionary[item]))        (ключ, обащаемся к словарю с выводом значения данного ключа)

# for (k,v) in dictionary.items():              это тот же вывод словаря:
#     print(k,v)                            k - отвечает за ключи, v - отвечает за значения

"""
            Множества
Содержит в себе уникальные эл-ы, не обязательно упорядочные.
Может содержать в 1 значения любых типов. Множества можно объединять, 
вычитать, пересекать. 
"""

# colors = {'red','grean','blue'}   создаем множество
# colors.add('red')                 при добавлении значения в множество - red не изменится, иначе добавит куда попало
# colors.remove('red')              удалить значение из множества
# colors.discard('red')             проверяет, есть ли это значение в множестве
#                       если такое значение есть, то удалит, иначе пропускает и не выводит ошибки

# colors.clear()                    очистить множество
# print(colors)                     после чего, мы увидим пустое множество: set()

#   Операции со множествами:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                                  c = {1, 2, 3, 5, 8}
# u = a.union(b)                                u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)                         i = {8, 2, 5}       те эл-ы, которые есть в обоих мн-ах (пересечение)
# dl = a.difference(b)                          dl = {1, 3}     вычитаем все одинакоые и выводим, что осталось в а
# dr = b.difference(a)                          dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))    {1, 21, 3, 13}
#          II        II            I     - Порядок действий, как и в математике 1- () и так далее

#        замороженное мно-во
#   мы не можем никак изменять
# a = {1, 3, 5}
# b = frozenset(a)
# print(b)

"""
        Генератор списков
"""
#   Создание списка от 1 до 100
# list_1 = [i for i in range(1, 101)]
#     Создание списка от 1 до 100 (только четные)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
#     Создаем список от 1 до 100, четные и с парой (кортеж)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
#     Создание списка от 1 до 100 (только четные) умноженные на 2 (принцип такой же и с другими мат. вычислениями)
# list_1 = [i * 2 for i in range(1, 101) if i % 2 == 0]