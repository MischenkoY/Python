import json
firma_list = []
forma_list = []
v_list = []
iz_list = []
profit_list = []
avg_list = []
my_dict = {}
my_dict1 = {}
f_list = []
with open('text_7.txt', 'r', encoding='utf8') as f_obj:
    for line in f_obj:
        firma, forma, v, iz = line.split()
        firma_list.append(firma)
        forma_list.append(forma)
        v_list.append(v)
        iz_list.append(iz)
    for i in range(len(iz_list)):
        j = float(v_list[i])
        k = float(iz_list[i])
        profit_list.append(j-k)
    for i in range(len(profit_list)):
        if profit_list[i] > 0:
            avg_list.append(profit_list[i])
    for i in range(len(profit_list)):
        a = firma_list[i]
        j = profit_list[i]
        my_dict[a] = j
    f_list.append(my_dict)
    f_list.append(my_dict1)
    my_dict1['average_profit'] = (sum(avg_list)/len(avg_list))
    print(f_list)
with open('text_7.json', 'w', encoding='utf8') as write_js:
    json.dump(f_list, write_js, indent=4, ensure_ascii=False)

    js_str = json.dumps(my_dict)