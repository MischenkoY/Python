from abc import ABC, abstractmethod


class clothes(ABC):

    def __init__(self, V, H):
        self.V = V
        self.H = H

    @property
    def my_method(self):
        return f'Общий расход ткани: {(((self.V / 6.5) + 0.5) + ((2 * self.H) + 0.3)):.2f}'

    @abstractmethod
    def __str__(self):
        pass


class coat(clothes):
    def __init__(self, V):
        self.V = V


    def __str__(self):
        return f'Расход ткани на польто: {(self.V / 6.5 + 0.5):.2f}'


class suit(clothes):
    def __init__(self, H):
        self.H = H

    def __str__(self):
        return f'Расход ткани на костюм: {(2 * self.H + 0.3):.2f}'


class property_my_metod(clothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    def __str__(self):
        pass


c_1 = coat(10)
c_2 = suit(15)
c_3 = property_my_metod(10, 15)
print(c_1)
print(c_2)
print(c_3.my_method)