def my_f(*args):
    '''
    Возвращает 2 значения
    Первое значение int,Второе значение bool
    '''
    my_list = []
    summa1 = 0
    ans1 = True
    for i in args:
        my_list.append(i.split())
        for j in sum(my_list, []):
            if j == 'q':
                ans1 = False
                return summa1, ans1
            elif j != 'q':
                summa1 = summa1 + int(j)
    return summa1, ans1


summa = 0
ans = True
while ans:
    summa2, ans = my_f(input("Введите несколько чисел разделенных пробелом (добавьте в конце строки q для выхода): "))
    summa = summa+summa2
    print(f"Сумма введенных элементов = {summa}")