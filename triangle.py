import unittest
def area(a, h):
    '''
        принимает целое число a и целое число h = сторона и высота треугольника
        возвращает значение площади целое число
        a(2) h(3) = a * h /2= 3
    '''
    return a * h / 2
def perimeter(a, b, c):
    '''
        принимает целое число a и целое число b и целое число c = стороны треугольника
        возвращает значение периметра целое число
        a(10) b(10) c(10) = a+b+c = 30
    '''
    return a + b + c

class TRIANGLETEST(unittest.TestCase):
    def test_int1(self):
        n = int(input("введите число для вычисления прямоугольника(целое и неотрицательное):"))
        n1 = int(input("введите число для вычисления прямоугольника(целое и неотрицательное):"))
        if ((n1 > 0 and n1 < 10 ** 9) and (n > 0 and n < 10 ** 9)):
            x = True
        else:
            x = False
        self.assertTrue(x)
    def test_int2(self):
        n = int(input("введите число для вычисления треугольника(целое и неотрицательное):"))
        n1 = int(input("введите число для вычисления треугольника(целое и неотрицательное):"))
        n2 = int(input("введите число для вычисления треугольника(целое и неотрицательное):"))
        ((n1 > 0 and n1 < 10 ** 9) and (n > 0 and n < 10 ** 9) and ((n2 > 0 and n2 < 10 ** 9)))
        if (n2 > 0 and n2 < 10 ** 9):
            x = True
        else:
            x = False
        self.assertTrue(x)
    def test_t_area(self):
        result = triangle.area(2, 3)
        self.assertEqual(result, 3)

    def test_t_peremiter(self):
        result = triangle.perimeter(10, 10, 10)
        self.assertEqual(result, 30)
