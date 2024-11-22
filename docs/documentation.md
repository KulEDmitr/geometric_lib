# Документация проекта Geometric_lib  
## Общее описание решения
В данном проекте представлены 4 файла: [rectanlge.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/rectangle.py), [circle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/circle.py), [triangle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/triangle.py), [square.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/square.py) . Каждый файл содержит в себе две функции, которые находят площадь и периметр для той фигуры, которая указана в названии.  
## Подробное описание файлов с функциями  
### Файл [rectangle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/rectangle.py)
Файл [rectangle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/rectangle.py) содержит две функции:  
1. Первая функция получает на вход стороны прямоугольника *a, b*, возвращает площадь прямоугольника, найденную по формуле **S = a*b**.  
```python  
def  area(a, b):
	'''Функция получет на вход стороны прямоугольника a, b, возвращает площадь прямоугольника. '''
	return a * b
```  
```python  
3 5  
15  
```  
2. Вторая функция получает на вход стороны прямоугольника *a, b*, возвращает периметр прямоугольника,  найденный по формуле **P = 2 * (a+b)**.
```python  
def  perimeter(a, b):
	'''Функция получает на вход стороны прямоугольника a, b, возвращает периметр прямоугольника. '''
	return  2*(a + b)
```  
```python   
2 6 
16  
```  
### Файл [circle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/circle.py)
Файл [circle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/circle.py) содержит две функции:  
1. Первая функция принимает на вход радиус окружности *r*, возвращает площадь окружности, найденный по формуле **S = $r^2$ * $pi$**
```python  
import math

def  area(r):
	'''Принимает на вход радиус окружности r, возвращает площадь окружности.'''
	return math.pi * r * r
```  
```python  
3  
28.274333882308138  
```  
2. Принимает на вход радиус окружности *r*, возвращает периметр окружности, найденный по формуле **S = 2 * $pi$ * r**.  
```python  
import math 

def  perimeter(r):
	''' Принимает на вход радиус окружности r, возвращает периметр окружности.'''
	return  2  * math.pi * r
```  
```python  
3  
18.84955592153876  
```    
### Файл [triangle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/triangle.py)
Файл [triangle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/triangle.py) содержит две функции:  
1. Первая функция получает на вход длину стороны *a* и длину высоты *h*, опущенной к стороне *a*, возвращает площадь треугольника, найденную по формуле **S = a * h /2**.
```python  
def  area(a, h):
	'''Функция получает на вход длину стороны a и длину высоты h, опущенной к стороне a, возвращает площадь треугольника'''
	return a * h /  2
```  
```python  
3 6  
9  
```  
2. Вторая функция получает на вход длины сторон *a, b, c*, возвращает периметр треугольника, найденный по формуле **S = a+b+c**.  
```python  
def  perimeter(a, b, c):
	'''Функция получает на вход длинs сторон a, b, c, возвращает периметр треугольника'''
	return a + b + c
```  
```python   
1 2 4 
7
```  
### Файл [square.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/square.py)
Файл [square.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/square.py) содержит две функции:  
1. Первая функция получает на вход сторону квадрата *a*, возвращает площадь квадрата, найденную по формуле **S = $a^2$**.
```python  
def  area(a):
	''' Функция получает на вход сторону квадрата a, возвращает площадь квадрата'''
	return a * a
```  
```python  
7  
49 
```  
2. Вторая функция функция получает на вход сторону квадрата *a*, возвращает периметр квадрата, найденный по формуле **S = 4 * a**.  
```python  
def  perimeter(a):
	''' Функция получает на вход сторону квадрата a, возвращает периметр квадрата'''
	return  4  * a
```  
```python   
3  
12 
```  
## История изменения проекта  
Коммиты:  
1. **8ba9aeb** : в самом первом коммите были добавлены файлы [circle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/circle.py) и [square.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/square.py).  
2. **d078c8d**: была добавлена папка Docs.  
3.  [**b2033e7**](https://github.com/KulEDmitr/geometric_lib/commit/b2033e7c45fea5b2f5744a55cf7c99a03c7312b4):добавлен файл [rectangle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/rectangle.py).  
4. [**b361dfe**](https://github.com/KulEDmitr/geometric_lib/commit/b361dfe6891c1fd718006f7d1452f872a78a049a):добавлен файл [triangle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/triangle.py).
5. [**5f50418**](https://github.com/KulEDmitr/geometric_lib/commit/5f50418b23354c367afc71d03105adf77bde674f): исправлены ошибки в файле [rectangle.py](https://github.com/ChekalkinS/geometric_lib/blob/new_features_427210/rectangle.py).