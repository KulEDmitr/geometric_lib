import unittest


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        from square import area
        res = area(0)
        self.assertEqual(res, 0)
        '''
            Происходит проверка расчета площади при поданом в функцию нуле
        '''

    def test_square_mul(self):
        from square import area
        res = area(10)
        self.assertEqual(res, 100)
        '''
            Проверяет расчет площади при подаче ненулевого аргумента в функию    
        '''

    def test_square_perimeter(self):
        from square import perimeter
        res = perimeter(10)
        self.assertEqual(res, 40)
        '''
            Проверяет расчет периметра при подаче ненулевого аргумента в функию    
        '''

    def test_zero_perimeter(self):
        from square import perimeter
        res = perimeter(0)
        self.assertEqual(res, 0)
        '''
            Происходит проверка расчета периметра при поданом в функцию нуле
        '''


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        from triangle import area
        res = area(10, 0)
        self.assertEqual(res, 0)
        '''
            Происходит проверка расчета площади при поданом в функцию нуле
        '''

    def test_perfect_mul(self):
        from triangle import area
        res = area(10, 10)
        self.assertEqual(res, 50)
        '''
            Проверяет расчет площади при подаче одинаковых аргументов в функию    
        '''

    def test_normal_mul(self):
        from triangle import area
        res = area(12, 10)
        self.assertEqual(res,60)
        '''
            Проверяет расчет площади при подаче различных аргументов в функию    
        '''

    def test_perfect_perimeter(self):
        from triangle import perimeter
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)
        '''
            Проверяет расчет периметра при подаче одинаковых аргументов в функию    
        '''

    def test_normal_perimeter(self):
        from triangle import perimeter
        res = perimeter(12, 10, 8)
        self.assertEqual(res, 30)
        '''
            Проверяет расчет периметра при подаче различных аргументов в функию    
        '''


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        from circle import area
        res = area(0)
        self.assertEqual(res, 0)
        '''
            Происходит проверка расчета площади при поданом в функцию нуле
        '''

    def test_circle_mul(self):
        from circle import area
        res = area(3)
        self.assertEqual(res, 28.274333882308138)
        '''
            Проверяет расчет площади при подаче ненулевого аргумента в функию    
        '''

    def test_circle_perimeter(self):
        from circle import perimeter
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)
        '''
            Проверяет расчет периметра при подаче ненулевого аргумента в функию    
        '''

    def test_zero_perimeter(self):
        from circle import perimeter
        res = perimeter(0)
        self.assertEqual(res, 0)
        '''
            Происходит проверка расчета периметра при поданом в функцию нуле
        '''


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        from rectangle import area
        res = area(10, 0)
        self.assertEqual(res, 0)
        '''
            Происходит проверка расчета площади при поданом в функцию нуле
        '''

    def test_square_mul(self):
        from rectangle import area
        res = area(10, 10)
        self.assertEqual(res, 100)
        '''
            Проверяет расчет площади при подаче одинаковых аргументов в функию    
        '''

    def test_rectangle_mul(self):
        from rectangle import area
        res = area(12, 10)
        self.assertEqual(res,120)
        '''
            Проверяет расчет площади при подаче различных аргументов в функию    
        '''

    def test_square_perimeter(self):
        from rectangle import perimeter
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
        '''
            Проверяет расчет периметра при подаче одинаковых аргументов в функию    
        '''

    def test_rectangle_perimeter(self):
        from rectangle import perimeter
        res = perimeter(12, 10)
        self.assertEqual(res, 44)
        '''
            Проверяет расчет периметра при подаче различных аргументов в функию    
        '''


if __name__ == '__main__':
    unittest.main()