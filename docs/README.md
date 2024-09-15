# Math formulas
## Python Math Module  
`math` — Mathematical functions and constants.  
Math module provides functions to deal with both basic operations such as addition(+), subtraction(-), multiplication(*), division(/) and advance operations like trigonometric, logarithmic, exponential functions.  
Math module provides various the value of various constants like pi, tau. Having such constants saves the time of writing the value of each constant every time we want to use it and that too with great precision. ***In this particular project from this module, the Pi constant is used to calculate the perimeter and area of a circle.***
```py
print(math.pi) -> 3.141592653589793
```
## Area
___
* ### Circle: S = πR²

__Пример вызова функции__
```py 
area(3) ==> 28.274333882308138 
```
__Пример ввода и вывода для функции__

|     Ввод     |       Вывод       |
|:------------:|:-----------------:|
|      3       |28.274333882308138 |
|      1.4     | 6.157521601035994 |

* ### Rectangle: S = ab

__Пример вызова функции__
```py 
area(2, 5.0) ==> 10.0
```
__Пример ввода и вывода для функции__

| Ввод  | Вывод  |
|:-----:|:------:|
| 7 10  |   70   |
| 2 5.0 |  10.0  |

* ### Square: S = a²

__Пример вызова функции__
```py 
area(10) ==> 100
```
__Пример ввода и вывода для функции__

| Ввод |       Вывод        |
|:----:|:------------------:|
|  10  |        100         |
| 4.6  | 21.159999999999997 |


* ### Triangle: S = ah/2

__Пример вызова функции__
```py 
area(1.4, 6.78) ==> 4.7459999999999996
```
__Пример ввода и вывода для функции__

|   Ввод   |       Вывод        |
|:--------:|:------------------:|
|   3 4    |        6.0         |
| 1.4 6.78 | 4.7459999999999996 |

## Perimeter
___
* ### Circle: P = 2πR

__Пример вызова функции__
```py 
perimiter(2.5) ==> 15.707963267948966
```
__Пример ввода и вывода для функции__

| Ввод |             Вывод              |
|:----:|:------------------------------:|
|  5   |       31.41592653589793        |
| 2.5  |       15.707963267948966       |

* ### Rectangle: P = 2(a + b)

__Пример вызова функции__
```py 
perimeter(3, 6) ==> 18
```
__Пример ввода и вывода для функции__

|  Ввод   | Вывод |
|:-------:|:-----:|
|   3 6   |  18   |
| 2.8 2.0 |  5.6  |

* ### Square: P = 4a 

__Пример вызова функции__
```py 
perimeter(2.8) ==> 11.2
```
__Пример ввода и вывода для функции__

| Ввод | Вывод |
|:----:|:-----:|
|  3   |  12   |
| 2.8  | 11.2  |

* ### Triangle: P = a+b+c

__Пример вызова функции__
```py 
perimeter(3.72, 1.34, 4.126) ==> 9.186
```
__Пример ввода и вывода для функции__

|      Ввод       | Вывод |
|:---------------:|:-----:|
|     11 4 7      |   22  |
| 3.72 1.34 4.126 | 9.186 |

## Tests

* ### Triangle

```python
def test_area(self):
        self.assertEqual(area(3, 4), 6.0)
        self.assertEqual(area(1.4, 0), 0)
        self.assertNotEqual(area(8.65, 4.183), 8)

    def test_perimeter(self):
        self.assertEqual(perimeter(110, 15.3, 6.2), 131.5)
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertNotEqual(perimeter(6.31, 4, 5.7), 10.2)
```

* ### Square

```python
def test_area(self):
        self.assertEqual(area(12), 144)
        self.assertEqual(area(2.5), 6.25)
        self.assertNotEqual(area(9.0), 81.1)

    def test_perimeter(self):
        self.assertEqual(perimeter(110), 440)
        self.assertEqual(perimeter(0), 0)
        self.assertNotEqual(perimeter(5.7), 21.1)
```

* ### Rectangle

```python
def test_area(self):
        self.assertEqual(area(7, 7), 49)
        self.assertEqual(area(2.4, 3.65), 8.76)
        self.assertNotEqual(area(8.65, 4.183), 8)

    def test_perimeter(self):
        self.assertEqual(perimeter(12, 3.5), 31)
        self.assertEqual(perimeter(2.25, 0), 4.5)
        self.assertNotEqual(perimeter(18, 3), 41)
```

* ### Circle

```python
def test_area(self):
        self.assertEqual(area(3), 28.274333882308138)
        self.assertEqual(area(1.4), 6.157521601035994)
        self.assertNotEqual(area(8.65), 16)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(2.5), 15.707963267948966)
        self.assertNotEqual(perimeter(6.31), 10.2)
```

## Commits
___

|    Commit     |                               Changes                                |
|:-------------:|:--------------------------------------------------------------------:|
| ***a785599*** | *Error in rectangle.py file fixed and python file triangle.py added* |
| ***da9ccc2*** |                   *Python file rectangle.py added*                   |
| ***d078c8d*** |                             *Docs added*                             |
| ***8ba9aeb*** |                      *Circle and square added*                       |