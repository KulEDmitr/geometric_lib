# Math formulas

Данный проект содержит файлы .py, в каждом из которых объявлены функции для подсчета площади и периметра **четырех
геометрических фигур**:

- Круг
- Прямоугольник
- Квадрат
- Треугольник

## Area formulas

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter formulas

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Functions

- ### circle.py
    - ##### area(r)
      Принимает неотрицательное число r - радиус окружности, возвращает площадь круга с радиусом r (произведение числа
      Пи на квадрат радиуса r):

      ```python
      print(area(5))
      -> 78.53981633974483
      ``` 
    - ##### perimeter(r)
      Принимает неотрицательное число r - радиус окружности, возвращает длину окружности с радиусом r (удвоенное
      произведение числа Пи на радиус r):

      ```python
      print(perimeter(5))
      -> 31.41592653589793
      ``` 

- ### rectangle.py
    - ##### area(a, b)
      Принимает 2 неотрицательных числа: a и b, - стороны прямоугольника. Возвращает площадь прямоугольника со сторонами
      a и b (произведение чисел a и b):

      ```python
      print(area(4, 5))
      -> 20
      ``` 
    - ##### perimeter(a, b)
      Принимает 2 неотрицательных числа: a и b, - стороны прямоугольника. Возвращает периметр прямоугольника со
      сторонами a и b (удвоенную сумму чисел a и b):

      ```python
      print(perimeter(4, 5))
      -> 18
      ``` 

- ### square.py
    - ##### area(a)
      Принимает неотрицательное число a - сторону квадрата, возвращает площадь квадрата со стороной a (квадрат числа a):

      ```python
      print(area(5))
      -> 25
      ``` 
    - ##### perimeter(a)
      Принимает неотрицательное число a - сторону квадрата, возвращает периметр квадрата со стороной a (произведение
      числа a на 4):

      ```python
      print(perimeter(5))
      -> 20
      ``` 

- ### triangle.py
    - ##### area(a, h)
      Принимает 2 неотрицательных числа: a и h, - основание треугольника и высота к этому основанию соответственно.
      Возвращает площадь треугольника с основанием a и высотой к этому основанию h (половина произведения чисел a и h):

      ```python
      print(area(5, 4))
      -> 10
      ``` 
    - ##### perimeter(a, b, c)
      Принимает 3 неотрицательных числа: a, b и c, - стороны треугольника. Возвращает периметр треугольника со
      сторонами (половина произведения чисел a и h):

      ```python
      print(perimeter(3, 4, 5))
      -> 12
      ``` 

## Unit Tests

Для проверки корректности работы вышеописанных функций были созданы unit тесты. В папке ``unit_tests`` находятся 4
файла с тестами для каждой фигуры соответственно:
- ``circle_test.py``
- ``rectangle_test.py``
- ``square_test.py``
- ``triangle_test.py``

Каждый из этих содержит тесты 4 типов:
- Тестирование функций при неправильном типе переданных аргументов
- Тестирование функций при недопустимом значении переданных аргументов
- Тестирование функций при нулевом значении переданных аргументов
- Тестирование функций на соответствие результата значению, посчитанному вручную

Успешность прохождения тестов:
- circle_test.py: ``2/8 = 25 %``
- rectangle_test.py: ``2/8 = 25 %``
- square_test.py: ``2/8 = 25 %``
- triangle_test.py: ``2/8 = 25 %``

## Project change history

- ``f49178e`` (HEAD -> create_unit_tests, origin/main, origin/HEAD, main) Added examples of calling of functions in all .py files and added last commit to project change history list in README.md
- ``df5c9ef`` Added last commits to project change history list in README.md
- ``1fdb837`` Updated README.md
- ``f57eaaa`` updated readme.md file: added description and examples of all functions from .py fies in the project,
  added project change history.
- ``3aceafd`` added comments to functions in all .py files
- ``c2aa33d`` (origin/main, origin/HEAD) Created triangle.py and fixed bug in calculating perimeter in rectangle.py
- ``f178690`` Created rectangle.py
- ``d078c8d`` L-03: Docs added
- ``8ba9aeb`` L-03: Circle and square added
