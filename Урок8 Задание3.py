class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


ans = ''
my_list1 = []
my_list = []
f_list = []
erro = False
while ans != 'stop':
    ans = input('Введите число: ')
    try:
        for i in ans:
            if i in '1234567890':
                num = i
                my_list1.append(num)
            else:
                erro = True
        if erro:
            raise MyError("Введено не число")
    except MyError as err:
        print(err)
    finally:
        buf = ''
        for i in range(len(my_list1)):
            num1 = buf + my_list1[i]
            buf = num1
        if buf != '':
            my_list.append(buf)
        my_list1.clear()
for i in my_list:
    f_list.append(int(i))
print(f'Список всех значений: {f_list}')