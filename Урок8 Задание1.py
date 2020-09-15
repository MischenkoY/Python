class DATA:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    @classmethod
    def dataclass(cls, data):
        data_list = []
        try:
            for i in data.split('-'):
                data_list.append(int(i))
            day = data_list[0]
            month = data_list[1]
            year = data_list[2]
            return cls(day, month, year)
        except (ValueError, IndexError):
            return print('Дата введена неверно')

    @staticmethod
    def datastatic(sm):
        try:
            if 0 < sm.day < 32:
                if 0 < sm.month < 13:
                    if 1 < sm.year < 9999:
                        return f'Дата введена верно'
                    else:
                        return f'Дата введена неверно'
                else:
                    return f'Дата введена неверно'
            else:
                return f'Дата введена неверно'
        except(AttributeError):
            return f'Ошибка'

    def __str__(self):
        return f'День: {self.day} Месяц: {self.month} Год: {self.year}'


my_1 = DATA.dataclass(input("Введите дату (цисло-месяц-год) "))
print(my_1)
print(DATA.datastatic(my_1))