#1 способ
def my_f(a1, a2, a3):
    if a2 >= a1 <= a3:
        # a1 наименьшее
        print(f"Сумма 2-ух наибольших чисел: {a2}+{a3}={a2+a3}")
    elif a1 >= a2 <= a3:
        # a2 наименьшее
        print(f"Сумма 2-ух наибольших чисел: {a1}+{a3}={a1+a3}")
    else:
        # a3 наименьшее
        print(f"Сумма 2-ух наибольших чисел: {a1}+{a2}={a1+a2}")


print("Введите 3 числа")
my_f(float(input("первое: ")), float(input("второе: ")), float(input("третье: ")))

#2 способ
def my_f1(a1, a2, a3):
    my_list1 = []
    my_list1.append(a1)
    my_list1.append(a2)
    my_list1.append(a3)
    print(f"Сумма 2-ух наибольших чисел: {sum(my_list1) - min(my_list1)}")

print("Введите 3 числа")
my_f1(float(input("первое: ")), float(input("второе: ")), float(input("третье: ")))