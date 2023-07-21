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


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        return self.width

    @side.setter
    def side(self, value):
        self.width = value
        self.height = value


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 5)
    print('width = ', my_rectangle.width)
    print('height = ', my_rectangle.height)
    print('area = ', my_rectangle.compute_area())
    my_rectangle.height = 4
    my_rectangle.width = 1
    print('dimensions changed.')
    print('width = ', my_rectangle.width)
    print('height = ', my_rectangle.height)
    print('area = ', my_rectangle.compute_area())
    my_sqaure = Square(5)
    print('square side = ', my_sqaure.side)
    print('area = ', my_sqaure.compute_area())
    my_sqaure.side = 10
    print('side changed')
    print('square side = ', my_sqaure.side)
    print('area = ', my_sqaure.compute_area())
