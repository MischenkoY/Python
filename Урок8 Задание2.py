class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите 1 число: ')
b = input('Введите 2 число: ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyError("На нуль делить нельзя")
    res = a / b
except ValueError:
    print("Введено не число")
except MyError as err:
    print(err)
else:
    print(f'Результат деления {a} / {b} = {round(res, 2)}')