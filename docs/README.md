# **Math formulas**
## **Area**
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## **Perimeter**
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = abc

## **Area funcion**
- Circle:
```
    На вход поступает число r, возвращает r^2*pi
    Пример:
        Ввод:
        r=2
        Вывод:
        area=12.56
```
- Rectangle:
```
    На вход поступают числа a и b, возвращает произведение a и b
    Пример:
        Ввод:
        a=2
        b=5
        Вывод:
        area=10
```
- Square:
```
    На вход поступает число a, возвращает a в квадрате
    Пример:
        Ввод:
        a=7
        Вывод:
        area=49
```
- Triangle:
```
    На вход поступают числа a и h, возвращает a умноженное на половину h
    Пример:
        Ввод:
        a=5
        h=4
        Вывод:
        area=10
```

## **Perimeter**
- Circle:
```
    На вход поступает число r, возвращает r*2*pi
    Пример:
        Ввод:
        r=4
        Вывод:
        perimeter=25.132
```
- Rectangle:
```
    На вход поступают числа a и b, возвращает удвоенное произведение a и b
    Пример:
        Ввод:
        a=5
        b=7
        Вывод:
        perimeter=24
```
- Square:
```
    На вход поступает число a, возвращает a умноженное на 4
    Пример:
        Ввод:
        a=2
        Вывод:
        perimeter=8
```
- Triangle:
```
    На вход поступают числа a, b и c, возвращает сумму этих чисел
    Пример:
        Ввод:
        a=2
        b=3
        c=4
        Вывод:
        perimeter=9
```

## **История изменения проекта с хешами комитов**
- 1 Комиит(8ba9aeb3cea847b63a91ac378a2a6db758682460): *L-03: Circle and square added*
- 2 Комиит(d078c8d9ee6155f3cb0e577d28d337b791de28e2): *L-03: Docs added*
- 3 Комиит(83b1514a0981b87a5ae52c2dbd8ca7cf2197201c): *добавлен файл rectangle*
- 4 Комиит(e691bddd3847f58264673bdeaf60d7930a2727b2): *Ошибка исправлена*
- 5 Коммит(b8d98a82dcb1e6bca25770def8c32bfb5c2284c4):  *Добавление комментариев*
- 6 Коммит(351eb9b4246a9342d5d8d15a928570cf6fff986a):  *Пробный пуш readme*
- 7 Коммит(72f9576458ba8443c1ab7fa27d98cb21ab480c73):  *Прбный пуш readme 2*

## **Общее решение**
- *Изучил текст лабы 2*
- *Изучил примечание в телеграм*
- *Изучил [Базовый синтаксис записи и форматирования](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)*
- *Добавил комментарии в файлы проекта*
- *Изменил файл README.md: добавил формулы для треугольника, расписал функции, добавил историю изменений*

## **Лаба 4**
*Добавлен тест для Triangle.py:*
```
import unittest
from triangle import area, perimeter  # Импортируем функции area и perimeter

class TriangleTestCase(unittest.TestCase):
    #корректные значения
    def test_area(self):
        self.assertEqual(area(5, 4), 10)  # Проверяем, area =  10
        self.assertEqual(area(0, 10), 0)  # Проверяем, area =  0
        self.assertEqual(area(10, 0), 0)  # Проверяем, area =  0
        self.assertEqual(area(3, 6), 9)    # Проверяем, area =  9

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3, 4), 9)  # Проверяем, perimeter =  9
        self.assertEqual(perimeter(1, 1, 1), 3)  # Проверяем, perimeter =  3
        self.assertEqual(perimeter(5, 5, 5), 15)  # Проверяем, perimeter =  15
        self.assertEqual(perimeter(0, 0, 0), 0)   # Проверяем, perimeter =  0

    # Тестируем некорректные входные данные 
    def test_invalid_area(self):
        with self.assertRaises(TypeError):
            area("5", 4)  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(TypeError):
            area(5, "4")  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(ValueError):
            area(-5, 4)   # Проверяем, что отрицательное основание вызывает ошибку
        with self.assertRaises(ValueError):
            area(5, -4)   # Проверяем, что отрицательная высота вызывает ошибку
        with self.assertRaises(ValueError):
            area(1e308, 1e308)  # Проверяем, что слишком большие числа вызывают ошибку

    def test_invalid_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("2", 3, 4)  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(TypeError):
            perimeter(2, "3", 4)  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(TypeError):
            perimeter(2, 3, "4")  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(-2, 3, 4)   # Проверяем, что отрицательная сторона вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(2, -3, 4)   # Проверяем, что отрицательная сторона вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(2, 3, -4)   # Проверяем, что отрицательная сторона вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(1e308, 1e308, 1e308)  # Проверяем, что слишком большие числа вызывают ошибку

if __name__ == '__main__':
    unittest.main()

```

