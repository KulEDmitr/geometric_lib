# Math formulas
В данной библиотеке вы найдете следующие формулы для работы с геометрическими фигурами:
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Work Directory
## circle.py
- Этот файл вы сможете найти по ссылке [circle.py](https://github.com/Jovenavr0/geometric_lib/blob/main/circle.py)
- При помощи него вы сможете посчитать периметр **def perimiter(r: int) -> float** и площадь **def area(r: int) -> float** заданного круга.


Примеры вызова функций:

 1. circle_area = area(5) circle_area = 78.53981633974483
 2. circle_perimeter = perimeter(5) circle_perimeter = 31.41592653589793

## rectangle.py
- Этот файл вы сможете найти по ссылке [rectangle.py](https://github.com/Jovenavr0/geometric_lib/blob/main/rectangle.py)
- При помощи него вы сможете посчитать периметр **def perimiter(a: int, b: int) -> int** и площадь **def area(a: int, b: int) -> int** заданного прямоугольника.


Примеры вызова функций:

 1. rectangle_area = area(5, 4) rectangle_area = 20
 2. rectangle_perimeter = perimeter(5, 4) rectangle_perimeter = 18

## square.py
- Этот файл вы сможете найти по ссылке [square.py](https://github.com/Jovenavr0/geometric_lib/blob/main/square.py)
- При помощи него вы сможете посчитать периметр **def perimiter(a: int) -> int** и площадь **def area(a: int) -> int** заданного квадрата.


Примеры вызова функций:

  1. square_area = area(5) square_area = 25
  2. square_perimeter = perimeter(5) square_perimeter = 20

## triangle.py
- Этот файл вы сможете найти по ссылке [triangle.py](https://github.com/Jovenavr0/geometric_lib/blob/main/triangle.py)
- При помощи него вы сможете посчитать периметр **def perimiter(a: int, b: int, c: int) -> int** и площадь **def area(a: int, h: int) -> float** заданного треугольника.


Примеры вызова функций:

  1. triangle_area = area(5, 10) triangle_area = 25.0
  2. triangle_perimeter = perimeter(5, 10, 6) triangle_perimeter = 21

Вызов unit тестов:

   python.exe -m unittest filename  

# История комитов

1. - commit 5b1350428dd971a7d12793398b2482aca8827575 (HEAD -> main, origin/main, origin/HEAD)
   - Author: Jovenavr0 <vvkarpenko2005@mail.ru>
   - Date:   Wed Nov 22 14:58:30 2023 +0300

       
    add unittest for all file in work directory


2. - commit 1f40aed550a2a3b3bb66879856ee386a67efdf6c
   - Author: Jovenavr0 <vvkarpenko2005@mail.ru>
   - Date:   Thu Sep 14 09:47:56 2023 +0300

  
    create new file triangle

3. - commit 5677a33e2843b06bbe77ea12ed0248af142578fe
   - Author: Jovenavr0 <vvkarpenko2005@mail.ru>
   - Date:   Thu Sep 14 09:46:55 2023 +0300

    
    create new file rectangle

4. - commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 
   - Author: smartiqa <info@smartiqa.ru>
   - Date:   Thu Mar 4 14:55:29 2021 +0300


    L-03: Docs added

5. - commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
   - Author: smartiqa <info@smartiqa.ru>
   - Date:   Thu Mar 4 14:54:08 2021 +0300

   
    L-03: Circle and square added




