class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, _height=5, massa=25):
        self._length = _length
        self._width = _width
        self._height = _height
        self.massa = massa

    def mass(self):
        print(f'Масса асфальта для покрытия {self._length*self._width}кв.м высотой {self._height}см = {(self._length*self._width*self._height*self.massa)/1000}т')

road1 = Road(20,5000)
road1.mass()