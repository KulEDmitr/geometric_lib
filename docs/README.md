# Geometric lib

## Общее описание решения

**Geometric lib** - библиотека, написанная на языке программирования Python, в которой описаны функции для вычисления площади и периметра таких фигур как: круг, квадрат, треугольник, прямоугольник.

## Описание каждой функции с примерами вызова

### circle.py

#### def area(r)

Находит площадь окружности.

Принимает число `r`, радиус окружности. 

##### Пример использования:

```
area(7) #Возвращает 153.93804002589985 
```

#### def perimeter(r)

Находит длину окружности.
	
Принимает число `r`, радиус окружности. 

##### Пример использования:
```
perimeter(7) #Возвращает 43.982297150257104
```

### rectangle.py

#### def area(a, b)

Находит площадь прямоугольника.

Принимает число `a`, `b`, стороны прямоугольника. 

##### Пример использования:
```
area(7, 8) #Возвращает 56
```

#### def perimeter(a, b)
Находит периметр прямоугольника.

Принимает число `a`, `b`, стороны прямоугольника. 

##### Пример использования:
```
area(7, 8) #Возвращает 30
```


### square.py
#### def area(a):

Находит площадь квадрата.
	
Принимает число `a`, сторону квадрата. 

##### Пример использования:
```
area(7) #Возвращает 49
```


#### def perimeter(a):

Находит периметр квадрата.
	
Принимает число `a`, сторону квадрата. 

##### Пример использования:
```
area(7) #Возвращает 28
```

### triangle.py

#### def area(a, h) 

Находит площадь треугольника.

Принимает числа `a`, `h`, сторону треугольника и высоту, опущенную к стороне. 

##### Пример использования:
```
area(7, 8) #Возвращает 28
```
	
	 

#### def perimeter(a, b, c) 

Находит периметр треугольника.

Принимает числа `a`, `b`, `c`, длины сторон треугольника. 

##### Пример использования:
```
perimeter(1, 2, 2) #Возвращает 5
```

## История изменения проекта с хешами комитов
- [`07ae08f62b03eed3f1d0a8cbad69cb65d050fd45`](https://github.com/kryaknut/geometric_lib/commit/07ae08f62b03eed3f1d0a8cbad69cb65d050fd45) (HEAD -> new_features_465899) added commets to functions
- [c9b07b3146ccbabcb9602f2a86d37cc84c5f674c`](https://github.com/kryaknut/geometric_lib/commit/c9b07b3146ccbabcb9602f2a86d37cc84c5f674c) (origin/new_features_465899) fixed bugs in rectangle.py
- [`448092304b004d4f8cf9a13d6bdb5440e11883d6`](https://github.com/kryaknut/geometric_lib/commit/448092304b004d4f8cf9a13d6bdb5440e11883d6) added new file triangle.py
- [`c1b4aa059b9bd8d5c6db7fed4a5fdbfe79ac31d0`](https://github.com/kryaknut/geometric_lib/commit/c1b4aa059b9bd8d5c6db7fed4a5fdbfe79ac31d0) added new file rectangle.py
- [`d078c8d9ee6155f3cb0e577d28d337b791de28e2`](https://github.com/kryaknut/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2) (origin/main, origin/HEAD) L-03: Docs added
- [`8ba9aeb3cea847b63a91ac378a2a6db758682460`](https://github.com/kryaknut/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460) L-03: Circle and square added
