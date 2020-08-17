ans = 'y'
n = 1
my_dict = dict({})
my_tuple = tuple([my_dict])
my_list = []
my_analitics = {}
my_analitics_list1 = []
my_analitics_list2 = []
my_analitics_list3 = []
while ans == 'y':
    my_dict = dict({'Название' : input("Введите название: "), 'цена': input("Введите цену: "), 'количество': input("Введите количество: "), 'ед': "шт"})
    my_list.append((n, my_dict))
    n += 1
    my_analitics_list1.append(my_dict['Название'])
    my_analitics_list2.append(my_dict['цена'])
    my_analitics_list3.append(my_dict['количество'])
    my_analitics['Название'] = my_analitics_list1
    my_analitics['цена'] = my_analitics_list2
    my_analitics['количество'] = my_analitics_list3
    my_analitics['ед'] = ['шт.']
    ans = input("Продолжить ввод?(y/n): ")
for i in my_list:
    print(i)
print("название:", my_analitics['Название'],'\n',"цена:", my_analitics['цена'],'\n',"количество:", my_analitics['количество'],'\n',"ед:",my_analitics['ед'])