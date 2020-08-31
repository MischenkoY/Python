from random import randint


class Car:
    def __init__(self, name, color, is_police=False, speed=0):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed


    def go(self):
        return f'{self.name} поехала'


    def stop(self):
        return f'{self.name} остановилась'


    def turn(self):
        turn = randint(1, 2)
        if turn == 1:
            return f'{self.name} повернула налево'
        if turn == 2:
            return f'{self.name} повернула направо'


    def show_speed(self):
        if self.speed < 1:
            self.speed = randint(1, 150)
            return f'Скорость {self.name} равна {self.speed}'
        return f'Скорость {self.name} равна {self.speed}'


class Towncar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return f'Превышение скорости, скорость {self.name} равна {self.speed}'
        else:
            return f'Скорость {self.name} равна {self.speed}'


class SportCar(Car):
    def show_speed(self):
        if self.speed < 1:
            self.speed = randint(1, 250)
            return f'Скорость {self.name} равна {self.speed}'
        return f'Скорость {self.name} равна {self.speed}'


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return f'Превышение скорости, скорость {self.name} равна {self.speed}'
        else:
            return f'Скорость {self.name} равна {self.speed}'


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


mazda = Towncar('mazda', 'green', False)
dodge = PoliceCar('dodge', 'black', True)
ferrari = SportCar('ferrari', 'Red', False)
opel = WorkCar('opel', 'White', False,)
print(mazda.name, mazda.color, mazda.go(), mazda.turn(), mazda.stop(), mazda.show_speed())
print(dodge.name, dodge.color, dodge.go(), dodge.turn(), dodge.stop(), dodge.show_speed(), dodge.police())
print(ferrari.name,ferrari.color, ferrari.go(), ferrari.turn(), ferrari.stop(), ferrari.show_speed())
print(opel.name, opel.color, opel.go(), opel.turn(), opel.stop(), opel.show_speed())