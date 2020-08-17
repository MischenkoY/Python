str1 = input("Введите строку из нескольких слов, разделённых пробелами: ")
list1 = []
j = 1
list1.append(str1.split())
for j, i in enumerate(list1[0]):
    print(f"{j+1} - {i [0:10]}")