# Geometric Lib
## Выполняет рассчет площади и периметра следющих фигур:
- круга - Circle.py
- прямоугольника - Rectangle.py
- квадрата - Square.py
- треугольника - Triangle.py

### Circle.py
#### Unit tests:
> Тесты проверяют правильность подсчета площади и периметра круга: в случае радиуса равного 0 и других

#### Code:
'''python
def area(r)
'''
> Принимает радиус круга и считает его площадь по формуле **S = πR<sup>2</sup>**
>
> Пример - area(2) = 12.56637

'''python
def perimeter(r)''' 
> Принимает радиус круга и считает его периметр по формуле **P = 2πR** 
>
> Пример - perimeter(2.5) = 7.85398

### Rectangle.py
#### Unit tests:
> Тесты проверяют правильность подсчета площади и периметра прямоугольника: в случае одной из сторон равной 0 и других  

#### Code:
'''python
def area(a, b)
'''
> Принимает длины сторон прямоугольника и считает его площадь по формуле **S = a * b**
>
> Пример - area(2, 6) = 12
'''python
def perimeter(a, b)
'''
> Принимает длины сторон пямоугольника и считает его периметр по формуле **P = 2 * (a + b)**
>
> Пример - perimeter(3, 1) = 8  
### Square.py
#### Unit tests:
> Тесты проверяют правильность подсчета площади и периметра квадрата: в случае одной из сторон равной 0 и других

#### Code:
'''python
def area(a)
'''
> Принимает длину стороны квадрата и считает площадь по формуле **S = a<sup>2</sup>**
>
> Пример - area(1.2) = 1.44
'''python
def perimeter(a)
''' 
> Принимает длину стороны квадрата и считает его периметр по формуле **P = 4 * a**
>
> Пример - perimeter(2) = 8

### Triangle.py
#### Unit tests:
> Тесты проверяют правильность подсчета площади и периметра прямоугольника: в случае одной или более из сторон равной 0 и других

#### Code:
'''python 
def area(a, h)
'''
> принимает длину стороны и высоты треугольник и считает его площадь треугольника по формуле **S = a * (h / 2)**
>
> Пример - area(2, 3) = 3
'''python
def perimeter(a, b, c)
'''
> Принимает длины сторон треугольника и считает его периметр по формуле **P = a + b + c**
>
> Пример - perimeter(1.1, 1.2, 2) = 4.3

## История коммитов:
* bd3a5cc (HEAD -> new_features_408571, origin/main, origin/HEAD, main) Fixed rectangle perimeter function
* b1eb0c0 Fixed rectangle perimeter function
* 0b8af4c Added new file - rectangle.py
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added
* 653eb14 (HEAD -> new_features_408571) Added more unit tests to check yml work
* a78fbba Merge pull request #1 from Kiksnol/new_features_408571_yml
* 2218521 Create main.yml
* 4901717 (origin/main, origin/HEAD, main) Delete .github/workflows directory
* 27c55b0 Create main.yml
* 729ee89 fixed unittests for circle.py
* 7e7191c updated readme file
* 865c156 added more unit tests
* 1fe3638 Merge branch 'new_features_408571' of https://github.com/Kiksnol/geometric_lib into new_features_408571
