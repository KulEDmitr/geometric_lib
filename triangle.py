import unittest, wolframalpha


def area(a, h):
    '''
    Принимает значение 2 переменных (сторона фигуры(треугольника) и высота фигуры(треугольника)) и выводит площадь фигуры(треугольника)
            Параметры: a(int/float) - десятичное число
                       b(int/float) - десятичное число
            Возвращаемое значение: area(int/float): десятичное число(площадь фигуры(треугольника))
            Пример вызова: print(area(3, 5)) -> 7.5
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Принимает значение 3 переменных (сторона фигуры(треугольника) и высота фигуры(треугольника)) и выводит периметр фигуры(треугольника)
            Параметры: a(int/float) - десятичное число
                       b(int/float) - десятичное число
                       c(int/float) - десятичное число
            Возвращаемое значение: perimeter(int/float): десятичное число(периметр фигуры(треугольника))
            Пример вызова: print(perimeter(3, 4, 5)) -> 12
    '''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_triangle_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    if a + b > c and a + c > b and b + c > a:
                        test_result = perimeter(a, b, c)
                    else:
                        test_result = 'not a possible triangle'
                    res = next(client.query(f'perimeter of triangle {a} {b} {c}').results).text
                    try:
                        res = int(res)
                    except Exception:
                        res = 'not a possible triangle'
                    self.assertEqual(test_result, res)
