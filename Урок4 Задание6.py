from itertools import count
from itertools import islice
from itertools import cycle


try:
    n = int(input("Введите число: "))
    my_list = []
    for el in islice(count(n), n*n):
        print(el)
        my_list.append(el)

    print(my_list)

    for i in islice(cycle(my_list), (len(my_list)*10)):
        print(i)
except ValueError:
    print("Введено не число")