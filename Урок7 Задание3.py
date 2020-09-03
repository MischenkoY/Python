class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell > other.cell:
            return Cell(self.cell - other.cell)
        else:
            return Cell(other.cell - self.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        if self.cell > other.cell:
            return Cell(self.cell // other.cell)
        else:
            return Cell(other.cell - self.cell)

    def __str__(self):
        return f'{self.cell}'

    def make_order(self, rows):
        row = ''
        for i in range(int(self.cell / rows)):
            row += f'{"*" * rows} \n'
        row += f'{"*" * (self.cell % rows) }'
        return Cell(row)


c_1 = Cell(13)
c_2 = Cell(12)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 // c_2)
print(c_1.make_order(3))