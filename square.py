import unittest, wolframalpha


def area(a):
    '''
    Принимает значение 1 переменной (сторона фигуры(квадрата)) и выводит площадь фигуры(квадрата)
            Параметры: a(int/float) - десятичное число
            Возвращаемое значение: area(int/float): десятичное число(площадь фигуры(квадрата))
            Пример вызова: print(area(7)) -> 49
    '''
    return a * a


def perimeter(a):
    '''
    Принимает значение 1 переменной (сторона фигуры(квадрата)) и выводит периметр фигуры(квадрата)
            Параметры: a(int/float) - десятичное число
            Возвращаемое значение: perimeter(int/float): десятичное число(периметр фигуры(квадрата))
            Пример вызова: print(perimeter(6)) -> 24
    '''

    return 4 * a


class SquareTestCase(unittest.TestCase):


    def test_all_square_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(30):
            test_result = area(a)
            res = next(client.query(f'area of square {a}').results).text
            self.assertEqual(test_result, int(res))
        for a in range(30):
            test_result = perimeter(a)
            res = next(client.query(f'perimeter of square {a}').results).text
            self.assertEqual(test_result, int(res))
