class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


class store:
    def __init__(self, office_equipment):
        self.office_equipment = office_equipment
        self.store_list = []

    def add_to_store(self):
        self.store_list.append(self.office_equipment)
        return self.store_list

    @staticmethod
    def menu():
        full_store = []
        ans = True
        erro = False
        while ans:
            try:
                print('*************\nМеню: \n1-добавить принтер\n2-добавить сканер\n3-добавить ксерокс\n4-показать что на складе\n5-выход\n*************')
                a = input('>>>')
                if a == '1':
                    print('Добавим принтер на склад')
                    name = input('Название: ')
                    price = float(input('Цена за 1 шт: '))
                    number = int(input('Количество: '))
                    form = input('Формат печати: ')
                    n1 = printer(name, price, number, form)
                    n_1 = store(n1.collect())
                    full_store.append(n_1.add_to_store())
                elif a == '2':
                    print('Добавим сканер на склад')
                    name = input('Название: ')
                    price = float(input('Цена за 1 шт: '))
                    number = int(input('Количество: '))
                    resolution = input('Разрешение сканера: ')
                    n2 = scanner(name, price, number, resolution)
                    n_2 = store(n2.collect())
                    full_store.append(n_2.add_to_store())
                elif a == '3':
                    print('Добавим ксерокс на склад')
                    name = input('Название: ')
                    price = float(input('Цена за 1 шт: '))
                    number = int(input('Количество: '))
                    scaling = input('Маштабирование: ')
                    n3 = xerox(name, price, number, scaling)
                    n_3 = store(n3.collect())
                    full_store.append(n_3.add_to_store())
                elif a == '4':
                    print(f'\nСейчас на складе: {full_store}\n')
                elif a == '5':
                    ans = False
                    print(f'\nСейчас на складе: {full_store}\n')
                else:
                    erro = True
                if erro:
                    raise MyErr('Ошибка меню! Попробуйте еще раз.')
            except MyErr as err:
                print(err)
            except ValueError:
                print('Ошибка ввода данных!')

class office_equipment:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number


class printer(office_equipment):
    def __init__(self, name, price, number, format):
        super().__init__(name, price, number)
        self.format = format
        self.printer_dict = {'Принтер': self.name, 'Цена за 1 шт': self.price,
                             'Количество': self.number, 'Формат печати': self.format}

    def collect(self):
        return self.printer_dict


class scanner(office_equipment):
    def __init__(self, name, price, number, resolution):
        super().__init__(name, price, number)
        self.resolution = resolution
        self.scanner_dict = {'Сканер': self.name, 'Цена за 1 шт': self.price,
                             'Количество': self.number, 'Разрешение сканера': self.resolution}

    def collect(self):
        return self.scanner_dict


class xerox(office_equipment):
    def __init__(self, name, price, number, scaling):
        super().__init__(name, price, number)
        self.scaling = scaling
        self.xerox_dict = {'Ксерокс': self.name, 'Цена за 1 шт': self.price,
                           'Количество': self.number, 'Маштабирование': self.scaling}

    def collect(self):
        return self.xerox_dict

m1 = store.menu()