class Shape:
    def compute_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def compute_area(self):
        return self._width * self._height


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 5)
    print(my_rectangle.compute_area())
