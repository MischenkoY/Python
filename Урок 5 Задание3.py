with open('text_3.txt', 'r', encoding="utf8") as f_obj:
    oklad = []
    name = []
    my_list = f_obj.read().split('\n')
    print(my_list, type(my_list))
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000.0:
            name.append(i[0])
        oklad.append(i[1])
    print(f'Оклад меньше 20000.0 {name}, средний оклад {sum(map(float, oklad)) / len(oklad)}')