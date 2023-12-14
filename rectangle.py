import unittest
def area(a, b):
    '''
        принимает целое число a и целое число b = стороны прямоугольника
        возвращает значение площади целое число
        a(10) b(2) = a * b = 20
    '''
    return a * b
def perimeter(a, b):
    '''
        принимает целое число a и целое число b = стороны прямоугольника
        возвращает значение периметра целое число
        a(10) b(2) = 2*(a+b) = 24
    '''
    return 2*(a + b)

class RECTANGLETEST(unittest.TestCase):
    def test_int1(self):
        n = int(input("введите число для вычисления прямоугольника(целое и неотрицательное):"))
        n1 = int(input("введите число для вычисления прямоугольника(целое и неотрицательное):"))
        if ((n1 > 0 and n1 < 10 ** 9) and (n > 0 and n < 10 ** 9)):
            x = True
        else:
            x = False
        self.assertTrue(x)
    def test_r_area_const(self):
        result = rectangle.area(10, 2)
        self.assertEqual(result, 20)

    def test_r_perimeter_const(self):
        result = rectangle.perimeter(10, 2)
        self.assertEqual(result, 24)