class ComplexNumber:
    def __init__(self, x1, y1=1):
        self.x1 = x1
        self.y1 = y1

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        x = self.x1 + other.x1
        y = self.y1 + other.y1
        if x != 0:
            if y > 0:
                return f'z = {x} + {y}i'
            if y == 0:
                return f'z = {x}'
            if y < 0:
                return f'z = {x} - {abs(y)}i'
        if x == 0:
            if y == 0:
                return f'z = 0'
            return f'z = {y}i'

    def __mul__(self,other):
        print(f'Произведение z1 и z2 равно')
        x = ((self.x1 * other.x1) - (self.y1 * other.y1))
        y = ((self.x1 * other.y1) + (self.y1 * other.x1))
        if x != 0:
            if y > 0:
                return f'z = {x} + {y}i'
            if y == 0:
                return f'z = {x}'
            if y < 0:
                return f'z = {x} - {abs(y)}i'
        if x == 0:
            if y == 0:
                return f'z = 0'
            return f'z = {y}i'

    def __str__(self):
        if self.y1 > 0:
            return f'z = {self.x1} + {self.y1}i'
        if self.y1 < 0:
            return f'z = {self.x1} - {abs(self.y1)}i'


z_1 = ComplexNumber(5, -3)
z_2 = ComplexNumber(-2, -9)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)