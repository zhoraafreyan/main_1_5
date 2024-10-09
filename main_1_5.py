immutable_var = 1, 3, True, 'клюква'
print(immutable_var)
#immutable_var[0] = 2
#Элементы кортежа изменить нельзя так как это был бы тот же самый список.
mutable_list = ([11, 65, 'Дробь'])
mutable_list[0] = 45
print(mutable_list)