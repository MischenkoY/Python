from random import randint
my_list = [randint(0, 100) for i in range(200)]
new_list = [my_list[i] for i in range(1, len(my_list), 1) if my_list.count(my_list[i]) == 1]
print(my_list)
print(new_list)

