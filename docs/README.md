# General description of the solution
For each figure: _**circle**, **rectangle**, **square**, **triangle**_. \
Created functions for calculating **area** and **perimeter** 
## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h) / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Examples of function calls
### Circle
#### Area:
Принимает 1 целочисленное значение - радиус окружности. \
Возвращает площадь этой окружности равную числу пи умноженному на r квадрат \
_Formula: **S = π * r * r**_
1.  input : 3
    output : 28.274333882308138
2.  input : 4
    output : 50.26548245743669
3.  input : 5
    output : 78.53981633974483
4.  input : 6
    output : 113.09733552923255
#### Perimeter:
Принимает 1 целочисленное значение - радиус окружности. \
Возвращает периметр окружности равный 2 умножить на число пи умножить на r. \
_Formula: **P = 2πr**_
1.  input : 3
    output : 18.84955592153876
2.  input : 4
    output : 25.132741228718345
3.  input : 5
    output : 31.41592653589793
4.  input : 6
    output : 37.69911184307752
### Rectangle:
#### Area:
Принимает числа a и b, где \
a - длина стороны прямоугольника. \
b - длина стороны прямоугольника не совпадающей со стороной a и не лежащей напротив неё. \
Возвращает площадь равную произведению этих сторон \
_Formula: **S = ab**_
1.  input : 3 2
    output : 6
2.  input : 4 3 
    output : 12 
3.  input : 5 4
    output : 20
4.  input : 6 5
    output : 30
#### Perimeter:
Принимает числа a и b, где \
a - длина стороны прямоугольника. \
b - длина стороны прямоугольника не совпадающей со стороной a и не лежащей напротив неё. \
Возвращает периметр прямоугольника равный удвоенной сумме сторон \
_Formula: **P = 2a + 2b**_
1.  input : 3 2
    output : 10
2.  input : 4 3 
    output : 14
3.  input : 5 4
    output : 18
4.  input : 6 5
    output : 22
### Square:
#### Area:
Принимает число а, возвращает а*а - площадь квадрата со стороной а. \
_Formula: **S = a * a**_
1.  input : 3 
    output : 9
2.  input : 4  
    output : 16
3.  input : 5 
    output : 25
4.  input : 6
    output : 36
#### Perimeter:
Принимает число a, возвращает a*4 - периметр квадрата со стороной a.\
_Formula: **P = 4a**_
1.  input : 3 
    output : 12
2.  input : 4  
    output : 16
3.  input : 5
    output : 20
4.  input : 6
    output : 24
### Triangle:
#### Area:
Принимает числа а и h, где \
а - сторона треугольника, \
h - высота проведенная к этой стороне. \
Возвращает площадь данного треугольника, посчитанную по формуле **a * h / 2** \
_Formula: **S = (a * h) / 2** _
1.  input : 3 2
    output : 3
2.  input : 4 3 
    output : 6
3.  input : 5 4
    output : 10
4.  input : 6 5
    output : 15
#### Perimeter:
Принимает числа a,b,c - стороны треугольника \
Возвращает периметр треугольника \
_Formula: **P = a + b +c**_
1.  input : 1 2 3
    output : 6
2.  input : 2 3 4
    output : 9
3.  input : 3 4 5
    output : 12
4.  input : 4 5 6
    output : 15
## Commits
commit: b03c70d5f2256e202e58067132623216e5578a88 
Author: Frustracoin <mr.timyr.temirov@mail.ru> 
Date:   Mon Sep 11 10:43:27 2023 +0300 

    fixed rectangle.py

commit: 7983af98777668669af2eaf5aa6f86c3a67bddb6 
Author: Frustracoin <mr.timyr.temirov@mail.ru> 
Date:   Mon Sep 11 10:39:45 2023 +0300

    new file triangle.py

commit: 64ab14597d068bfa6d6e2c29c28470182c84b5f1 
Author: Frustracoin <mr.timyr.temirov@mail.ru> 
Date:   Mon Sep 11 10:36:21 2023 +0300

    new file rectangle.py

commit: d078c8d9ee6155f3cb0e577d28d337b791de28e2 
Author: smartiqa <info@smartiqa.ru> 
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460 
Author: smartiqa <info@smartiqa.ru> 
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

