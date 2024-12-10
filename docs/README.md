# Документация

## Math formulas
**Area**

 - Circle: S = πR²

 - Rectangle: S = ab

 - Square: S = a²

 - Triangle: S = 1/2 * a * h 

**Perimeter**

 - Circle: P = 2πR

 - Rectangle: P = 2a + 2b

 - Square: P = 4a

 - Triangle: P = a + b + c 

## Общее описание решения:
Добавила комментарии, объясняющие каждую функцию, закоммитила, создала каталог докс где в файле ридми указала формулы а
также в общих чертах описала действия

(I added comments explaining each function, committed, created a docks directory where I specified formulas in the readmi
file and also described the actions in general terms)


## Описание ф-ций:
def area_square(a):
    
    Вычисляет площадь квадрата по длине стороны.

    Параметры:
        a (int/float): длина стороны квадрата

    Возвращаемое значение:
        float: площадь квадрата

    Пример вызова:
        area_square(4) -> 16
    

def perimeter_square(a):

    Вычисляет периметр квадрата по длине стороны.

    Параметры:
        a (int/float): длина стороны квадрата

    Возвращаемое значение:
        float: периметр квадрата

    Пример вызова:
        perimeter_square(4) -> 16


def area_circle(r):

    Вычисляет площадь окружности по радиусу.

    Параметры:
        r (int/float): радиус окружности

    Возвращаемое значение:
        float: площадь окружности

    Пример вызова:
        area_circle(5) -> 78.53981633974483



def perimeter_circle(r):
    
    Вычисляет периметр (длину) окружности по радиусу.

    Параметры:
        r (int/float): радиус окружности

    Возвращаемое значение:
        float: длина окружности

    Пример вызова:
        perimeter_circle(5) -> 31.41592653589793


def area_triangle(a, h):
    
    Вычисляет площадь треугольника исходя из его высоты и длинны стороны, к которой проведена высота.
    
    Параметры:
        a (int/float): длинна стороны
        h (int/float): высота

    Возвращаемое значение:
        float: площадь треугольника

    Пример вызова:
        area_triangle(5, 3) -> 7.5
    

def perimeter_triangle(a, b, c):

    Вычисляет периметр треугольника исходя из длины его сторон.
    
    Параметры:
        a (int/float): длинна стороны
        b (int/float): длинна стороны
        c (int/float): длинна стороны

    Возвращаемое значение:
        float: периметр треугольника

    Пример вызова:
        area_triangle(5, 3, 4) -> 12
    
def area_rectangle(a, b):

    Вычисляет площадь прямоугольника из длин его сторон.
    
    Параметры:
        a (int/float): длинна прямоугольника
        b (int/float): высота прямоугольника

    Возвращаемое значение:
        float: площадь прямоугольника

    Пример вызова:
        area_triangle(5, 3) -> 15
    

def perimeter_rectangle(a, b):
    
    Вычисляет периметр прямоугольника из длин его сторон.
    
    Параметры:
        a (int/float): длинна прямоугольника
        b (int/float): высота прямоугольника

    Возвращаемое значение:
        float: периметр треугольника

    Пример вызова:
        area_triangle(5, 3) -> 16



## Хэши
9458ba7f266c717c49c1fe361882f54b738bae20 Added .idea/workspace.xml to .gitignore

d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added

8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added


## Ссылки на коммиты

- [Добавление в гитигнор](https://github.com/KulEDmitr/geometric_lib/commit/9458ba7f266c717c49c1fe361882f54b738bae20)
- [Удаление папки docks](https://github.com/KulEDmitr/geometric_lib/commit/c28c51815e0fbb8b7bc3a7ec8a5fff9da99792f4)
- [Добавление новой ветки](https://github.com/KulEDmitr/geometric_lib/commit/3f6df9f8f85d0aa8e7fd782e81edb16f565e2c7e)
- [Исправление формата readme](https://github.com/KulEDmitr/geometric_lib/commit/04e61aeaed33e0ab0aeb57011cb8c57557c436bd)

# File Testing

## Описание
Проект содержит функции для вычисления площади и периметра фигур с набором тестов для проверки корректности работы функций.

## Тестирование
В тестах проверяется поведение функций на граничных и некорректных данных, включая:
- Нулевые значения сторон
- Отрицательные значения
- Чрезмерно большие значения
- Некорректные типы данных

## Запуск тестов
Используйте команду `python -m unittest test_rectangle.py` для запуска тестов для файла rectangle.py.
Используйте команду `python -m unittest test_square.py` для запуска тестов для файла square.py.
Используйте команду `python -m unittest test_circle.py` для запуска тестов для файла circle.py.
Используйте команду `python -m unittest test_triangle.py` для запуска тестов для файла triangle.py.

