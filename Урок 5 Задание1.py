f_obj = open("my_file.txt", "w", encoding="utf8")
a = input("Введите данные(для завершения ввода введите пустую строку): ")
while True:
    if a != '':
        f_obj.writelines(f"{a}\n")
        a = input("Введите данные(для завершения ввода введите пустую строку): ")
    else:
        f_obj.close()
        break