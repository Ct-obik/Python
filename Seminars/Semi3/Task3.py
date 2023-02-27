# Напишите программу для печати всех уникальных
# значений в словаре. { 1:2, 3:4 , 2:2 } -> 4,2

dict_ = {1: 2, 3: 4, 2: 2}
list_ = []
for item in dict_:
    list_.append(dict_[item])
print(set(list_))
