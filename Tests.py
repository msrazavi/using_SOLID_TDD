import unittest
from AreaCalculatorProject import Shape, Square, Rectangle


class TestShapes(unittest.TestCase):
    def test_rectangle(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.compute_area(), 12)

        r.width = 5
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.compute_area(), 20)

        r.height = 5
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.compute_area(), 25)

    def test_square(self):
        s = Square(3)
        self.assertEqual(s.side, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.compute_area(), 9)

        s.side = 5
        self.assertEqual(s.side, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.compute_area(), 25)


if __name__ == '__main__':
    unittest.main()
