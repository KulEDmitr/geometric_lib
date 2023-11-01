import math, unittest, wolframalpha

'''
    Библиотека математических функций, констант  и т.д.
'''


def area(r):
    '''
    Принимает значение 1 переменной (радиус фигуры(круга)) и выводит площадь фигуры(круга)
            Параметры: r(int/float) - десятичное число
            Возвращаемое значение: area(float): десятичное число(площадь фигуры(круга))
            Пример вызова: print(area(6)) -> 113.04
    '''

    return math.pi * r * r


def perimeter(r):
    '''
    Принимает значение 1 переменной (радиус фигуры(круга)) и выводит периметр фигуры(круга)
            Параметры: r(int/float) - десятичное число
            Возвращаемое значение: perimetr(float): десятичное число(периметр фигуры(круга))
            Пример вызова: print(perimeter(4)) -> 25.12
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):

    def test_circle_area_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(2, 10):
            test_result = round(area(a))
            res = next(client.query(f'area of circle with radius {a}').results).text
            self.assertEqual(test_result, round(float(res[res.rfind("≈") + 1::])))

    def test_circle_perimeter_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(2, 10):
            test_result = round(perimeter(a))
            res = next(client.query(f'perimeter of circle with radius {a}').results).text
            self.assertEqual(test_result, round(float(res[res.rfind("≈") + 1::])))
