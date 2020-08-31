class Stationery:
    err = False

    def __init__(self, title):
        self.title = title
        if self.title == 'Pen':
            print('Ручка')
        elif self.title == 'Pencil':
            print('Карандаш')
        elif self.title == 'Handle':
            print('Маркер')
        else:
            print('Неизвестная канцелярская принадлежность')
            self.err = True


    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        super().draw()
        if self.err:
            return f'Ошибка! Возьмите другую канцелярская принадлежность'
        elif self.title == 'Pen':
            return f'Вы взяли {self.title} отрисовка ручкой'
        else:
            return f'Ошибка! Возьмите другую канцелярская принадлежность'


class Pencil(Stationery):
    def draw(self):
        super().draw()
        if self.err:
            return f'Ошибка! Возьмите другую канцелярская принадлежность'
        elif self.title == 'Pencil':
            return f'Вы взяли {self.title} отрисовка карандашом'
        else:
            return f'Ошибка! Возьмите другую канцелярская принадлежность'


class Handle(Stationery):
    def draw(self):
        super().draw()
        if self.err:
            return f'Ошибка! Возьмите другую канцелярская принадлежность'
        elif self.title == 'Handle':
            return f'Вы взяли {self.title} отрисовка маркером'
        else:
            return f'Ошибка! Возьмите другую канцелярская принадлежность'


stat1 = Pencil('Pencil')
print(stat1.draw())
print()
stat2 = Pen('Pen')
print(stat2.draw())
print()
stat3 = Handle('Handle')
print(stat3.draw())
print()
stat4 = Pen('Pencil')
print(stat4.draw())
print()
stat5 = Pencil('notebook')
print(stat5.draw())