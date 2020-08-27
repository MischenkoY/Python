f_obj = open('text_5.txt', 'w+', encoding="utf8")
my_list = []
a = input("Введите набор чисел, разделенных пробелами: ")
f_obj.writelines(a)
f_obj.seek(0)
my_list.append(f_obj.readlines())
for i in my_list[0]:
    i = i.split()
    summa = sum(map(float, i))
print(f'Сумма всех элементов в файле = {summa}')
f_obj.close()