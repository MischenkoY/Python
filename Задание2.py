list1 = [7, 'text', 12.3, None, True, 1+3j, [1, 2, 3], ('a', 'b', 'c')]
list2 = []
ans = 'y'
j = 0
while ans == 'y':
    list1.append(input('Введите новый элемент для списка: '))
    ans = input('Ввести еще?(y/n): ')
if ans == 'n':
    list2 = list1.copy()
for i in range(1, len(list1), 2):
    list1[j], list1[j + 1] = list1[j + 1], list1[j]
    j += 2
print(list2)
print(list1)