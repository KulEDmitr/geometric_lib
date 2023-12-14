import unittest
def area(a):
    '''
        принимает целое число a  =  сторона квадрата
        возвращает значение площади целое число
        a (4) = a*a =16
    '''
    return a * a
def perimeter(a):
    '''
        принимает целое число a  =  сторона квадрата
        возвращает значение периметра целое число
        a(4)=a*4 = 16
    '''
    return 4 * a
class SQUARETEST(unittest.TestCase):
    def test_int(self):
        n = int(input("введите число для вычисления квадрата(целое и неотрицательное):"))
        if(n > 0 and n < 10**9):
            x = True
        else:
            x = False
        self.assertTrue(x)
    def test_s_area(self):
        result = square.area(4)
        self.assertEqual(result, 16)

    def test_s_perimeter(self):
        result = square.area(4)
        self.assertEqual(result, 16)
