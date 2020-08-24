from sys import argv
script_name, a, b, c = argv
try:
    a = int(a)
    b = int(b)
    c = int(c)
    d = (a*b)+c
    print("Выработка в часах: ", a, "\n" "Cтавка в час: ", b, "\n" "Премия: ", c, "\n" "Заработная плата сотрудника: ", d)
except ValueError:
    print("Введено не число")