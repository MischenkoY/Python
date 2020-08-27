my_dict = {}
lec_list = []
lec_list1 = []
prac_list = []
prac_list1 = []
lab_list = []
lab_list1 = []
my_list = []
y_p_list = []
y_p_list1 = []
with open('text_6.txt', 'r', encoding='utf8') as f_obj:
    for line in f_obj:
        y_p, lec, prac, lab = line.split()
        y_p_list.append(y_p)
        lec_list.append(lec)
        lab_list.append(lab)
        prac_list.append(prac)
    for i in range(len(lec_list)):
        if lec_list[i] == '-':
            lec_list.remove(lec_list[i])
            lec_list.insert(i, '0')
    for i in range(len(lab_list)):
        if lab_list[i] == '-':
            lab_list.remove(lab_list[i])
            lab_list.insert(i, '0')
    for i in range(len(prac_list)):
        if prac_list[i] == '-':
            prac_list.remove(prac_list[i])
            prac_list.insert(i, '0')
    for i in lec_list:
        i = i.split('(л)')
        lec_list1.append(i[0])
    for i in lab_list:
        i = i.split('(лаб)')
        lab_list1.append(i[0])
    for i in prac_list:
        i = i.split('(пр)')
        prac_list1.append(i[0])
    for i in y_p_list:
        i = i.split(':')
        y_p_list1.append(i[0])
    for i in range(len(y_p_list1)):
        a = y_p_list1[i]
        j = int(lec_list1[i])
        k = int(lab_list1[i])
        t = int(prac_list1[i])
        my_dict[a] = (j + k + t)
    print(f'Общее количество часов по предметам : \n {my_dict}')