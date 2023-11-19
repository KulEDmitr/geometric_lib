# Geometric Lib
## Выполняет рассчет площади и периметра следющих фигур:
- круга - Circle.py
- прямоугольника - Rectangle.py
- квадрата - Square.py
- треугольника - Triangle.py

### Circle.py
'''python
def area(r)
'''
> Принимает радиус круга и считает его площадь по формуле **S = πR<sup>2</sup>**
> Пример - area(2) = 12.56637

'''python
def perimeter(r)''' 
> Принимает радиус круга и считает его периметр по формуле **P = 2πR**
> Пример - perimeter(2.5) = 7.85398

### Rectangle.py
'''python
def area(a, b)
'''
> Принимает длины сторон прямоугольника и считает его площадь по формуле **S = a * b**
> Пример - area(2, 6) = 12
'''python
def perimeter(a, b)
'''
> Принимает длины сторон пямоугольника и считает его периметр по формуле **P = 2 * (a + b)**
> Пример - perimeter(3, 1) = 8  
### Square.py
'''python
def area(a)
'''
> Принимает длину стороны квадрата и считает площадь по формуле **S = a<sup>2</sup>**
> Пример - area(1.2) = 1.44
'''python
def perimeter(a)
''' 
> Принимает длину стороны квадрата и считает его периметр по формуле **P = 4 * a**
> Пример - perimeter(2) = 8

### Triangle.py
'''python 
def area(a, h)
'''
> принимает длину стороны и высоты треугольник и считает его площадь треугольника по формуле **S = a * (h / 2)**
> Пример - area(2, 3) = 3
'''python
def perimeter(a, b, c)
'''
> Принимает длины сторон треугольника и считает его периметр по формуле **P = a + b + c**
> Пример - perimeter(1.1, 1.2, 2) = 4.3

## История коммитов:
* bd3a5cc (HEAD -> new_features_408571, origin/main, origin/HEAD, main) Fixed rectangle perimeter function
* b1eb0c0 Fixed rectangle perimeter function
* 0b8af4c Added new file - rectangle.py
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added