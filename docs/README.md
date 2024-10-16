# Документация

## Math formulas
Area
Circle: S = πR²
Rectangle: S = ab
Square: S = a²
Perimeter
Circle: P = 2πR
Rectangle: P = 2a + 2b
Square: P = 4a

## General description of the solution:
I added comments explaining each function, committed, created a docks directory where I specified formulas in the readmi
file and also described the actions in general terms

(добавила комментарии, объясняющие каждую функцию, закоммитила, создала каталог докс где в файле ридми указала формулы а
также в общих чертах описала действия)


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


## Хэши
9458ba7f266c717c49c1fe361882f54b738bae20 Added .idea/workspace.xml to .gitignore
d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added


## Ссылки на коммиты
Добавление в гитигнор https://github.com/KulEDmitr/geometric_lib/commit/9458ba7f266c717c49c1fe361882f54b738bae20
Удаление папки docks https://github.com/KulEDmitr/geometric_lib/commit/c28c51815e0fbb8b7bc3a7ec8a5fff9da99792f4
Добавление новой ветки https://github.com/KulEDmitr/geometric_lib/commit/3f6df9f8f85d0aa8e7fd782e81edb16f565e2c7e
Исправление формата readme https://github.com/KulEDmitr/geometric_lib/commit/04e61aeaed33e0ab0aeb57011cb8c57557c436bd