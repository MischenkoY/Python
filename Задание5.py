my_list = [7, 5, 3, 3, 2]
a = int(input("Введите новый элемент рейтинга: "))
for i in range(len(my_list)):
    if a > my_list[i]:
        my_list.insert(i, a)
        break
    elif a <= my_list[-1]:
        my_list.append(a)
        break
print("Пользователь ввел число", a, "Результат:", my_list)
