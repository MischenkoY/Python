from itertools import count
from math import factorial

try:
    n = int(input("Введите число: "))


    def fact():
        for el in count(n):
            yield factorial(el)


    x = 1
    for i in fact():
        if x <= n:
            print(f"Факториал: {x}! = {i}")
            x += 1
        else:
            break
except ValueError:
    print("Введено не число")