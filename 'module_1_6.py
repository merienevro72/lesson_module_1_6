#работа со словарями
my_dict = {'Ваня':1999, 'Юля':1997, 'Никита':2006}
print(my_dict)
print(my_dict.get('Никита'))
print(my_dict.get('Вова'))
my_dict.update({'Роман':2019, 'Саша':2020})
print(my_dict)
a = my_dict.pop ('Юля')
print(my_dict)
print(a)
print(my_dict)
#работа с множествами
my_set = {111,111,'числа',333,111,True,333, True}
print (my_set)
(my_set.add (777),my_set.add ('дроби'))
print (my_set)
my_set.discard(333)
print(my_set)