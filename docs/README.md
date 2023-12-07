# Geometric_lib
Geometric_Lib предоставляет возможность работать со следующими геометрическими фигурами:
- [Круг](https://github.com/Artem010999/geometric_lib#Круг)
- [Квадрат](https://github.com/Artem010999/geometric_lib#Квадрат)
- [Прямоугольник](https://github.com/Artem010999/geometric_lib#Прямоугольник)
- [Треугольник](https://github.com/Artem010999/geometric_lib#Треугольник)
  
Также в нём реализована проверка работы функций с помощью тестов:
- [Unittests](https://github.com/Artem010999/geometric_lib#Unittests)

# Круг
Для круга выполнены следующие операции: вычислении площади и периметра круга. Ссылка на [полный код](https://github.com/Artem010999/geometric_lib/blob/main/circle.py) 
```python
import math 

def area(r): # Возвращает площадь круга
    return math.pi * r * r

Input: 7
Output: 153.93804002589985
```

```python
import math

def perimeter(r): # Возвращает периметр круга
    return 2 * math.pi * r

Input: 10
Output: 62.83185307179586
```

# Квадрат
Для квадрата выполнены следующие операции: вычислении площади и периметра квадрата. Ссылка на [полный код](https://github.com/Artem010999/geometric_lib/blob/main/square.py)
```python
def area(a): # Возвращает площадь квадрата
    return a * a

Input: 11
Output: 121
```

```python
def perimeter(a, b): # Вовзвращает периметр квадрата
    return 4 * a

Input: 4
Output: 16
```

# Прямоугольник
Для прямоугольника выполнены следующие операции: вычислении площади, периметра прямоугольника, а также его диагональ. Ссылка на [полный код](https://github.com/Artem010999/geometric_lib/blob/main/rectangle.py)
```python
def area(a, b): # Возвращает площадь прямоугольника
    return a * b

Input: 5, 10
Output: 50
```

```python
def perimeter(a, b): # Вовзвращает периметр прямоугольника
    return (a + b) * 2

Input: 2, 6
Output: 16
```

```python
def diagonal(a, b): # Возвращает диагональ прямоугольника
	return (a ** 2 + b ** 2) ** 0.5

Input: 3, 4
Output: 5

```

# Треугольник
Для треугольника выполнены следующие операции: вычислении площади и периметра треугольника. Ссылка на [полный код](https://github.com/Artem010999/geometric_lib/blob/main/triangle.py)
```python
def area(a, h): # Возвращает площадь треугольника
	return a * h / 2

Input: 5, 4
Output: 10
```

```python
def perimeter(a, b, c): # Вовзвращает периметр треугольника
    return a + b + с

Input: 6, 8, 10
Output: 24
```

# Unittests
Также покрыл выполнение данных функций для всех геометрических фигур unit-тестами, используя соответствующую библиотеку. Пример использования для файла triangle.py:
```python
import unittest


class TriangleTestCase(unittest.TestCase):

	def test_0_area(self):
		area_result = area(11, 0)
		self.assertEqual(area_result, 0)

	def test_1_area(self):
		area_result = area(123456789, 9876543210)
		self.assertEqual(area_result, (123456789 * 9876543210) / 2)

	@unittest.expectedFailure
	def test_2_area(self):
		area_result = area("abcd", 1)
		self.assertEqual(area_result, TypeError)

	def test_3_area(self):
		area_result = area(11, -1)
		self.assertEqual(area_result, TypeError)

	def test_0_perimeter(self):
		perimeter_result = perimeter(0, 0, 0)
		self.assertEqual(perimeter_result, 0)

	def test_1_perimeter(self):
		perimeter_result = perimeter(123456789, 9876543210, 1)
		self.assertEqual(perimeter_result, 123456789 + 9876543210 + 1)

	@unittest.expectedFailure
	def test_2_perimeter(self):
		perimeter_result = perimeter("a", 2, "c")
		self.assertEqual(perimeter_result, TypeError)

	def test_3_perimeter(self):
		perimeter_result = perimeter(1, -2, 3)
		self.assertEqual(perimeter_result, TypeError)
```

# История изменения проекта:
```
* 10429f7a9d79acf7a3358a42369ef5ad63a4807d (HEAD -> main) Добавил описания работы функций для файлов: rectangle.py, triangle.py, circle.py и square.py. Также описал пример вызова каждой функции из каждого файла.
* ad2926eb5f879bf1921f7d78808cbd7b3c51e68a Добавил комментарии к функциям в файле Rectangle.py и сделал вывод данных функций.
* d6541236a112cfd8a255fff1e438c9d9081cb15c (origin/main, origin/HEAD) Добавлен файл: triangle.py и исправлена ошибка в вычислении периеметра в файле: rectangle.py
* 6c2b8300ad086886b4b08bce0779340a4f2103bd Добавил новый файл: rectangle.py
```


# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h) / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Diagonal
- Rectangle: c = √(a² + b²)
