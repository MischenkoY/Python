v = float(input('Введите значение выручки: '))
iz = float(input('Введите значение издержек: '))
if v<iz:
    print(f"Фирма работает в убыток = {v - iz}")
else:
    print(f"Прибыль фирмы = {v-iz} , рентабельность выручки = {((v-iz)/v)}")
    s = int(input('Введите число сотрудников: '))
    print(f"Прибыль фирмы в расчете на одного сотрудника = {(v-iz)/s}")
