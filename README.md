# Общая информация о библиотеке

 Библиотека позволяет вычислять параметры геометрических фигур по входным данным ( стороны, радиус, высота ): 
 - Площадь
 - Периметр


# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Описание функций с примерами вывода

## Файл **circle.py**
### area(r):
 - Возвращает площадь круга с радиусом r
 - Параметры:
	- r (int): десятичное число - радиус
 - Возвращаемое значение:
	- area(r): площадь круга
 - int(r) = 3; pi * r * r= 28.274333882308138
### perimetr(r):
 - Возвращает длину окружности с радиусом r
 - Параметры:
	- r (int): десятичное число - радиус
 - Возвращаемое значение:
	- perimetr(r): длина окружности r
 - int(r) = 3; 2 * pi * r = 18.84955592153876
## Файл **rectangle.py**
### area(a,b):
 - Возвращает площадь прямоугольника со сторонами a, b
 - Параметры:
	- a (int): первое десятичное целое число, сторона прямоугльника
	- b (int): второе десятичное целое число, сторона прямоугольника
 - Возвращаемое значение:
	- area(a,b): площадь прямоугольника - произведение параметров a,b
 - int(a) = 4, int(b) = 5; a * b = 20
### perimetr(a,b):
 - Возвращает периметр прямоугольника со сторонами a, b
 - Параметры:
	- a (int): первое десятичное целое число, сторона прямоугльника
	- b (int): второе десятичное целое число, сторона прямоугольника
 - Возвращаемое значение:
	- area(a,b): периметр прямоугольника - удвоенная сумма параметров 
a,b
 - int(a) = 4, int(b) = 5; 2 * (a + b) = 18
## Файл **square.py**
### area(a):
 - Возвращает площадь квадрата со стороной a
 - Параметры:
	- a (int): первое десятичное целое число, сторона квадрата
 - Возвращаемое значение:
	- area(a): площадь квадрата - квадрат параметра a
 - int(a) = 5; a * a = 25
### perimetr(a,b):
 - Возвращает периметр квадрата со стороной a
 - Параметры:
	- a (int): первое десятичное целое число, сторона прямоугльника
 - Возвращаемое значение:
	- perimetr(a): периметр квадрата - длина стороны квадрата умноженная на 4
 - int(a) = 5 -> a * 4 = 20
## Файл **triangle.py**
### area(a,h):
 - Возвращает площадь треугольника с длиной основания a и высотой h
 - Параметры:
	- a (int): первое десятичное целое число, длина основания треугольника
	- h (int): второе десятичное целое число, длина высоты треугольника
 - Возвращаемое значение:
	- area(a): площадь треугольника - половина произведения a и h
 - int(a) = 10, int(h) = 12; a * h * 0.5 = 60
### perimetr(a,b,c):
 - Возвращает периметр треугольника со сторонами a,b,c
 - Параметры:
	- a (int): первое десятичное целое число, сторона треугольника
	- b (int): первое десятичное целое число, сторона треугольника
	- c (int): первое десятичное целое число, сторона треугольника
 - Возвращаемое значение:
	- perimetr(a): периметр треугольника со сторонами a,b,c
 - int(a) = 3, int(b) = 4, int(c) = 5; a + b + c = 12
# История изменений проекта по хешам:
4df22582c92dc6053acf2d97bd1f8bd791;
53d95a31090f84dbec7fb47c7fbc4eb85139427a;
d078c8d9ee6155f3cb0e577d28d337b791de28e2;
8ba9aeb3cea847b63a91ac378a2a6db758682460;
0c41bc213fc6fa38173cf8b2c21a76ab313149d7;
