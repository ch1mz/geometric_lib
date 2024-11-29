import unittest
import math
import circle
import triangle
import  rectangle
import square

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_million_area(self):
        res = square.area(1000000)
        self.assertEqual(res, 1000000000000)

    def test_hundred_perimeter(self):
        res = square.perimeter(100)
        self.assertEqual(res, 400)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)


class circleTestCase(unittest.TestCase):
    def test_area_hundred(self):
        res = circle.area(100)
        self.assertEqual(res, math.pi * 10000)
    def test_perimeter_2million(self):
        res = circle.perimeter(2147000)
        self.assertEqual(res, 4294000*math.pi)
    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res,0)
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)

    def test_million_area(self):
        res = triangle.area(1000000, 1)
        self.assertEqual(res, 500000)

    def test_hundred_perimeter(self):
        res = triangle.perimeter(100, 200, 300)
        self.assertEqual(res, 600)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(0,0)
        self.assertEqual(res, 0)

    def test_million_area(self):
        res =rectangle.area(1000000,0)
        self.assertEqual(res, 0)

    def test_hundred_perimeter(self):
        res = rectangle.perimeter(100,0)
        self.assertEqual(res, 200)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0,0)
        self.assertEqual(res, 0)
