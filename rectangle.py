import wolframalpha, unittest


def area(a, b):
    '''
    Принимает значения двух переменных(стороны фигуры(прямоугольника)) и выводит площадь(прямоугольника)
            Параметры: a(int/float) - первое десятичное число
                       b(int/float) - второе десятичное число
            Возвращаемое значение: area(int/float): десятичное число(площадь фигуры(прямоугольника))
            Пример вызова: print(area(3, 4)) -> 12
    '''

    return a * b


def perimeter(a, b):
    '''
    Принимает значения двух переменных(стороны фигуры(прямоугольника)) и выводит периметр(прямоугольника)
            Параметры: a(int/float) - первое десятичное число
                       b(int/float) - второе десятичное число
            Возвращаемое значение: perimeter(int/float): десятичное число(периметр фигуры(прямоугольника))
            Пример вызова: print(perimeter(5, 4)) -> 18
    '''

    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):

    def test_rectangle_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(2):
            for b in range(2):
                test_result = area(a, b)
                res = next(client.query(f'area of rectangle {a}, {b} = ').results).text
                self.assertEqual(test_result, int(res))
                test_result = perimeter(a, b)
                res = next(client.query(f'perimeter of rectangle {a}, {b} = ').results).text
                self.assertEqual(test_result, int(res))
