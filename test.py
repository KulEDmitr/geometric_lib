import unittest
from square import *
from rectangle import *
from circle import *
import math

class AreaRectangleTestCase(unittest.TestCase):
    # Проверяет, корректно ли функция возвращает ошибку при отрицательных значениях
    def testAreaRectangleNegative(self):
        res = areaRectangle(-5, 4)
        self.assertEqual(res, "Incorrect input")

    # Проверяет, правильно ли функция возвращает 0, если одно из значений равно 0
    def testAreaRectangleZero(self):
        res = areaRectangle(10, 0)
        self.assertEqual(res, 0)

    # Проверяет, возвращает ли функция правильный результат для значений 10 и 10
    def testAreaRectangleTen(self):
        res = areaRectangle(10, 10)
        self.assertEqual(res, 100)

    # Проверяет, корректно ли функция работает с дробными значениями
    def testAreaRectangleDouble(self):
        res = areaRectangle(2.5, 4)
        self.assertEqual(res, 10)

    # Проверяет, выводит ли функция ошибку при передаче символа
    def testAreaRectangleChar(self):
        res = areaRectangle('a', 3)
        self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче строки
    # def testAreaRectangleString(self):
    #     res = areaRectangle(4, "string")
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче слишком большого числа
    def testAreaRectangleBigInteger(self):
        res = areaRectangle(10000000000000000000000000000000000000000000000, 3)
        self.assertEqual(res, "Incorrect input")


class PerimeterRectangleTestCase(unittest.TestCase):
    # Проверяет, корректно ли функция возвращает ошибку при отрицательных значениях
    # def testPerimeterRectangleNegative(self):
    #     res = perimeterRectangle(-5, 4)
    #     self.assertEqual(res, "Incorrect input")

    # Проверяет, правильно ли функция возвращает 0, если одно из значений равно 0
    # def testPerimeterRectangleZero(self):
    #     res = perimeterRectangle(10, 0)
    #     self.assertEqual(res, 0)

    # Проверяет, возвращает ли функция правильный результат для значений 10 и 10
    def testPerimeterRectangleTen(self):
        res = perimeterRectangle(10, 10)
        self.assertEqual(res, 40)

    # Проверяет, корректно ли функция работает с дробными значениями
    def testPerimeterRectangleDouble(self):
        res = perimeterRectangle(2.5, 4)
        self.assertEqual(res, 13)

    # Проверяет, выводит ли функция ошибку при передаче символа
    # def testPerimeterRectangleChar(self):
    #     res = perimeterRectangle('a', 3)
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче строки
    # def testPerimeterRectangleString(self):
    #     res = perimeterRectangle(4, "string")
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче слишком большого числа
    # def testPerimeterRectangleBigInteger(self):
    #     res = perimeterRectangle(10000000000000000000000000000000000000000000000, 3)
    #     self.assertEqual(res, "Incorrect input")


class AreaCircleTestCase(unittest.TestCase):
    # Проверяет, выводит ли функция ошибку при отрицательном значении радиуса
    # def testAreaCircleNegative(self):
    #     res = areaCircle(-5)
    #     self.assertEqual(res, "Incorrect input")

    # Проверяет, правильно ли функция возвращает 0, если радиус равен 0
    def testAreaCircleZero(self):
        res = areaCircle(0)
        self.assertEqual(res, 0)

    # Проверяет, возвращает ли функция правильный результат для радиуса 10
    def testAreaCircleTen(self):
        res = areaCircle(10)
        self.assertEqual(res, 100 * math.pi)

    # Проверяет, корректно ли функция работает с дробными значениями
    def testAreaCircleDouble(self):
        res = areaCircle(2.5)
        self.assertEqual(res, 2.5 * 2.5 * math.pi)

    # Проверяет, выводит ли функция ошибку при передаче символа
    # def testAreaCircleChar(self):
    #     res = areaCircle('a')
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче строки
    # def testAreaCircleString(self):
    #     res = areaCircle("string")
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче слишком большого числа
    # def testAreaCircleBigInteger(self):
    #     res = areaCircle(10000000000000000000000000000000000000000000000)
    #     self.assertEqual(res, "Incorrect input")


class PerimeterCircleTestCase(unittest.TestCase):
    # Проверяет, выводит ли функция ошибку при отрицательном значении радиуса
    # def testPerimeterCircleNegative(self):
    #     res = perimeterCircle(-5)
    #     self.assertEqual(res, "Incorrect input")

    # Проверяет, правильно ли функция возвращает 0, если радиус равен 0
    def testPerimeterCircleZero(self):
        res = perimeterCircle(0)
        self.assertEqual(res, 0)

    # Проверяет, возвращает ли функция правильный результат для радиуса 10
    def testPerimeterCircleTen(self):
        res = perimeterCircle(10)
        self.assertEqual(res, 20 * math.pi)

    # Проверяет, корректно ли функция работает с дробными значениями
    def testPerimeterCircleDouble(self):
        res = perimeterCircle(2.5)
        self.assertEqual(res, 5 * math.pi)

    # Проверяет, выводит ли функция ошибку при передаче символа
    # def testPerimeterCircleChar(self):
    #     res = perimeterCircle('a')
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче строки
    # def testPerimeterCircleString(self):
    #     res = perimeterCircle("string")
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче слишком большого числа
    # def testPerimeterCircleBigInteger(self):
    #     res = perimeterCircle(10000000000000000000000000000000000000000000000)
    #     self.assertEqual(res, "Incorrect input")


class AreaSquareTestCase(unittest.TestCase):
    # Проверяет, выводит ли функция ошибку при отрицательном значении стороны
    # def testAreaSquareNegative(self):
    #     res = areaSquare(-5)
    #     self.assertEqual(res, "Incorrect input")

    # Проверяет, правильно ли функция возвращает 0, если сторона равна 0
    def testAreaSquareZero(self):
        res = areaSquare(0)
        self.assertEqual(res, 0)

    # Проверяет, возвращает ли функция правильный результат для стороны 10
    def testAreaSquareTen(self):
        res = areaSquare(10)
        self.assertEqual(res, 100)

    # Проверяет, корректно ли функция работает с дробными значениями
    def testAreaSquareDouble(self):
        res = areaSquare(2.5)
        self.assertEqual(res, 6.25)

    # Проверяет, выводит ли функция ошибку при передаче символа
    # def testAreaSquareChar(self):
    #     res = areaSquare('a')
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче строки
    # def testAreaSquareString(self):
    #     res = areaSquare("string")
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче слишком большого числа
    # def testAreaSquareBigInteger(self):
    #     res = areaSquare(10000000000000000000000000000000000000000000000)
    #     self.assertEqual(res, "Incorrect input")


class PerimeterSquareTestCase(unittest.TestCase):
    # Проверяет, выводит ли функция ошибку при отрицательном значении стороны
    # def testPerimeterSquareNegative(self):
    #     res = perimeterSquare(-5)
    #     self.assertEqual(res, "Incorrect input")

    # Проверяет, правильно ли функция возвращает 0, если сторона равна 0
    # def testPerimeterSquareZero(self):
    #     res = perimeterSquare(0)
    #     self.assertEqual(res, 0)

    # Проверяет, возвращает ли функция правильный результат для стороны 10
    def testPerimeterSquareTen(self):
        res = perimeterSquare(10)
        self.assertEqual(res, 40)

    # Проверяет, корректно ли функция работает с дробными значениями
    def testPerimeterSquareDouble(self):
        res = perimeterSquare(2.5)
        self.assertEqual(res, 10)

    # Проверяет, выводит ли функция ошибку при передаче символа
    # def testPerimeterSquareChar(self):
    #     res = perimeterSquare('a')
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче строки
    # def testPerimeterSquareString(self):
    #     res = perimeterSquare("string")
    #     self.assertEqual(res, "Incorrect input")

    # # Проверяет, выводит ли функция ошибку при передаче слишком большого числа
    # def testPerimeterSquareBigInteger(self):
    #     res = perimeterSquare(10000000000000000000000000000000000000000000000)
    #     self.assertEqual(res, "Incorrect input")


if __name__ == '__main__':
    unittest.main()
