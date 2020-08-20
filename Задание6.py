def int_func(*args):
    '''
    Возвращает строку
    '''
    my_list = []
    my_list1 = []
    str1 = ''
    for i in args:
        my_list1.append(i)
        my_list = (list(my_list1[0]))
        print(my_list)
    if 97 <= ord(my_list[0]) <= 122:
        n_e = ord(my_list[0]) - 32
        my_list.pop(0)
        my_list.insert(0, chr(n_e))
    for i in range(0, len(my_list), 1):
        if ord(my_list[i]) == 32 and 97 <= ord(my_list[i+1]) <= 122:
            n_e = ord(my_list[i+1]) - 32
            my_list.pop(i+1)
            my_list.insert(i+1, chr(n_e))
            print(my_list)
    for i in my_list:
        str1 = str1 + i
    return str1


print(int_func(input("Введите строку из слов, разделенных пробелом: ")))