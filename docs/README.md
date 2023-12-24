# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a*h/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Описание проекта
Данный проект позволяет вычислять площади различных геометрических выпуклых фигур (круг, прямоугольник, квадрат и треугольник)

# Описание файлов проекта
## circle.py
### area
Данная функция на вход получает значение радиуса круга и возвращает его площадь  
Пример вызова функции area:

``` python
s = area(3)   
print(s)
```
В данном случае будет выведено значение **9pi**

### perimeter

Данная функция на вход получает значение радиуса круга и возвращает его периметр  
Пример вызова:

``` python
p = perimeter(3)
print(p)
```
В данном случае будет выведено значение **6pi**

## rectangle.py
### area
Данная функция на вход получает два значения длин сторон прямоугольника и возвращает его площадь  
Пример вызова функции area:

``` python
s = area(2, 3)
print(s)
```

В данном случае будет выведено значение **6**

### perimeter
Данная функция получает на вход два значения длин сторон прямоугольника и возвращает его периметр  
Пример вызова:

``` python
p = perimeter(2, 3)
print(p)
```

В данном случае будет выведено значение **10**

## square.py
### area
Данная функция на вход получает значение длины стороны квадрата и возвращает его площадь  
Пример вызова:

``` python
s = area(2)
print(s)
```

В данном случае будет выведено значение **4**

### perimeter
Данная функция получает на вход значение длины стороны квадрата и возвращает его периметр  
Пример вызова:

``` python
p = perimeter(2)
print(p)
```

В данном случае будет выведено значение **8**

## triangle.py
### area
Данная функция получает на вход два значения (длина стороны треугольника и длина высота, проведенной к этой стороне) и выводит площадь треугольника  
Пример вызова:

``` python
s = area(2, 3)
print(s)
```

В данном случае будет выведено значение **3**

### perimeter
Данная функция получает на вход три значения длин сторон треугольника и возвращает значение его площади  
Пример вызова:

``` python
p = perimeter(1, 2, 3)
print(p)
```

В данном случае будет выведено значение **6**

# История изменения проекта
* commit 16a5c69b50d6765d26320ecc5da57b15e36d4997 (HEAD -> main)
  - Author: eklkeklk <komissarovaeleni@yandex.ru>
  - Date: Thu Oct 12 09:38:22 2023 +0300  
  
    `Fixed documentary in circle.py, triangle.py, rectangle.py, square.py`


* commit 2d7ae70af0135b9fbcc5775b8eefd05d59ec6cc3 (HEAD -> main, origin/main, origin/HEAD)
  - Author: eklkeklk <komissarovaeleni@yandex.ru>  
  - Date:   Wed Oct 11 22:28:49 2023 +0300  

    `add readme.md file and add documentary changes to circle.py, rectangle.py, triangle.py, square.py`  


* commit eee4581b17920a5047bea43055733fa7e5526846
  - Author: Komissarova Elena <komissarovaeleni@yandex.ru>  
  - Date:   Wed Sep 27 20:34:37 2023 +0300  
  
    `error fixed`


* commit 1940def525fa84eedfee11f84e8e5fb15632954d  
  - Author: Komissarova Elena <komissarovaeleni@yandex.ru>  
  - Date:   Wed Sep 27 20:26:30 2023 +0300      
      
    `new file added`  
  

* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
  - Author: smartiqa <info@smartiqa.ru>
  - Date:   Thu Mar 4 14:55:29 2021 +0300  
  `:...skipping...`
  

* commit 2d7ae70af0135b9fbcc5775b8eefd05d59ec6cc3 (HEAD -> main, origin/main, origin/HEAD)

  - Author: eklkeklk <komissarovaeleni@yandex.ru>
  - Date:   Wed Oct 11 22:28:49 2023 +0300
  
       `add readme.md file and add documentary changes to circle.py, rectangle.py, triangle.py, square.py`
  

* commit eee4581b17920a5047bea43055733fa7e5526846
  - Author: Komissarova Elena <komissarovaeleni@yandex.ru>
  - Date:   Wed Sep 27 20:34:37 2023 +0300
  
       `error fixed`


* commit 1940def525fa84eedfee11f84e8e5fb15632954d
  - Author: Komissarova Elena <komissarovaeleni@yandex.ru>
  - Date:   Wed Sep 27 20:26:30 2023 +0300
  
       `new file added`
  
  
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
  - Author: smartiqa <info@smartiqa.ru>
  - Date:   Thu Mar 4 14:55:29 2021 +0300
  
       `L-03: Docs added`  
  `:...skipping...`
  

* commit 2d7ae70af0135b9fbcc5775b8eefd05d59ec6cc3 (HEAD -> main, origin/main, origin/HEAD)
  - Author: eklkeklk <komissarovaeleni@yandex.ru>
  - Date:   Wed Oct 11 22:28:49 2023 +0300
  
       `add readme.md file and add documentary changes to circle.py, rectangle.py, triangle.py, square.py`
  

* commit eee4581b17920a5047bea43055733fa7e5526846
  - Author: Komissarova Elena <komissarovaeleni@yandex.ru>
  - Date:   Wed Sep 27 20:34:37 2023 +0300
  
       `error fixed`
  

* commit 1940def525fa84eedfee11f84e8e5fb15632954d
  - Author: Komissarova Elena <komissarovaeleni@yandex.ru>
  - Date:   Wed Sep 27 20:26:30 2023 +0300
  
       `new file added`
  
  
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
  - Author: smartiqa <info@smartiqa.ru>
  - Date:   Thu Mar 4 14:55:29 2021 +0300
  
    `L-03: Docs added`
  
* commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  - Author: smartiqa <info@smartiqa.ru>
  - Date:   Thu Mar 4 14:54:08 2021 +0300

      `L-03: Circle and square added`

