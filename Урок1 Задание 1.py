n1 = float(input('Введите 1 число : '))
n2 = float(input('Введите 2 число : '))
a = input('Введите символ операции (+,-,*,/) : ')
if a == '+' or a == '-' or a == '/' or a == '*':
    if a == '+':
        n = n1 + n2
    elif a == '-':
        n = n1 - n2
    elif a == '/':
        n = n1 / n2
    elif a == '*':
        n = n1 * n2
    print(n1, a , n2, '=' ,n,)
else:
    print('Неверный символ операции')
s1 = input('Как вас зовут? : ')
s2 = input('Сколько вам лет? : ')
print(s1 , s2)