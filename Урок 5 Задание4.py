my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []

with open('text_4.txt', 'r', encoding="utf8") as f_obj:
    for i in f_obj:
        i = i.split(' -')
        my_list.append(my_dict[i[0]] + ' -' + i[1])
    print(my_list)

with open('text_4_new.txt', 'w', encoding="utf8") as f_obj_2:
    f_obj_2.writelines(my_list)