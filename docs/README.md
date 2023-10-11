# Solutions:
## В данной библиотеке присутствуют функции для вычисления площади и периметра квадрата, прямоугольнмка, круго и треугольника

# Description of functions:
## Circle:


import math

>Подключаем библиотеку math для работы с числом Pi

def area(r):
>Принимает число r, возращает произведение из квадрата r и числа Pi;
> Например: area(10) вернет 314.15...
   
 return math.pi * r * r


def perimeter(r):
>Принимает число r, возращает произведение из 2*r и числа 
> Например: perimetr(8) вернет 16 * 3,1415.. 
   
 return 2 * math.pi * r

## Rectangle:



def area(a, b): 
> Функция принимает две стороны прямоугольника, возвращает его площадь;
> Например: area(5, 8) вернет 40"
    
return a * b 

def perimeter(a, b): 
>Функция принимает две стороны прямоугольника, возвращает его периметр;
> Например: perimetr(5, 8) вернет 36`
    
return 2*(a + b) 


## Square:

def area(a, b): 
>Принимает числа a и b, возвращает произведение a на b ;
> Например: area(5) вернет 25
    return a * b 

def perimeter(a, b): 
>Принимает числа a и b, возвращает произведение удвоенное a на b;
> Например: perimetr(8) вернет 32
    
return 2*a + 2*b 


## Triangle:
def area(a, h): 
>Функция принимает два катета треугольника, возвращает его площад;  
> Например: area(5, 8) вернет 20
    
return a * h / 2 

def perimeter(a, b, c):
>Функция принимает три стороны треугольника, возвращает его периметр; 
> Например: perimetr(5, 8, 4) вернет 17

    
return a + b + c


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

    added new file```
