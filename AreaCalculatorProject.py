class Shape:
    def compute_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def compute_area(self):
        return self._width * self._height


class Square(Shape):
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    def compute_area(self):
        return self.side * self.side


if __name__ == '__main__':
    pass
