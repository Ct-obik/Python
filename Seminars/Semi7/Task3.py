# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращают True, если это так. Если значение характеристики для разных
# объектов отличается - то False. Для пустого набора объектов, функция должна
# возвращать True. Аргумент characteristic - это функция, которая принимает
# объект и вычисляет его характеристику.

def char(x):
    return x % 2


def same_by(characteristic, objects):
    objects = set(map(characteristic, objects))
    if len(objects) == 1:
        return True
    return False


mass = [1, 1, 0, 1]
print(same_by(char, mass))
