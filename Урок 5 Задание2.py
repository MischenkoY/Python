f_obj = open("my_file.txt", encoding="utf8")
content = f_obj.read()
print(f"Содержимое файла: \n{content}")
f_obj.seek(0)
content = f_obj.readlines()
print(f"Количество строк в файле: {len(content)}")
my_list = list(content)
slo = 1
k = 1
for i in range(len(my_list)):
    for j in my_list[i]:
        if j == ' ':
            slo += 1
        elif j == '\n':
            print(f'Количество слов в {k} строке = {slo}')
            slo = 1
            k += 1
        elif k == len(content):
            slo = 1
            print(f'Количество слов в {len(content)} строке = {slo} ')
f_obj.close()