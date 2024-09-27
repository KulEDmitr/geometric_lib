# Solutions:
### В данной библиотеке присутствуют функции для вычисления площади и периметра квадрата, прямоугольнмка, круга и треугольника
### Библиотека покрыта unit тестами, для вызова тестирования определенного файла необходимо в консоли прописать комнаду: 
- python.exe -m unittest название_файла.py

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: a + b + c


# Description of functions:
## Circle:


import math

>Подключаем библиотеку math для работы с числом Pi

def area(r):
>Принимает число r, возращает произведение из квадрата r и числа Pi;
> 
> Например: area(10) вернет 314.15...
   
 


def perimeter(r):
>Принимает число r, возращает произведение из 2*r и числа 
> 
> Например: perimetr(8) вернет 16 * 3,1415.. 
   
 

## Rectangle:



def area(a, b): 
> Функция принимает две стороны прямоугольника, возвращает его площадь;
> 
> Например: area(5, 8) вернет 40"
    
return a * b 

def perimeter(a, b): 
>Функция принимает две стороны прямоугольника, возвращает его периметр;
> 
> Например: perimetr(5, 8) вернет 36`
    


## Square:

def area(a): 
>Принимает числo a, возвращает произведение a на a ;
> 
> Например: area(5) вернет 25



def perimeter(a: 
>Принимает числo a, возвращает произведение удвоенное a + a;
> 
> Например: perimetr(8) вернет 32
    


## Triangle:
def area(a, h): 
>Функция принимает два катета треугольника, возвращает его площад;  
> 
> Например: area(5, 8) вернет 20
    

def perimeter(a, b, c):
>Функция принимает три стороны треугольника, возвращает его периметр; 
> 
> Например: perimetr(5, 8, 4) вернет 17



# History with commits hashes:
```
commit fe166492f18d681e2180bec5b70536421d55b913 (origin/main, origin/HEAD)
Author: unknown <gligaandrej@gmail.com>
Date:   Sat Sep 30 14:41:01 2023 +0300

    Исправил ошибку в файле rectangle.py

commit 7bdaea2e1c1a32f2cf8e085fdd45611d6a955bcd (new_features_408448)
Author: unknown <gligaandrej@gmail.com>
Date:   Fri Sep 22 14:40:02 2023 +0300

    fixed error

commit 823d20bcf394a223b091acac7d60f090e4daf262
Author: unknown <gligaandrej@gmail.com>
Date:   Fri Sep 22 14:07:07 2023 +0300

    fixed error

commit c8addd81a777e94388ec070e6a5af8717a8cd2b8
Author: unknown <gligaandrej@gmail.com>
Date:   Fri Sep 22 14:04:36 2023 +0300

    added new file
```
