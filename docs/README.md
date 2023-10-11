# Solutions:
## Add functions for circle, rectangle, square and triangle

# Description of functions:
## Circle:


import math

- Подключаем библиотеку math для работы с числом Pi

def area(r):
- Принимает число r, возращает произведение из квадрата r и числа Pi   
    return math.pi * r * r


def perimeter(r):
 - Принимает число r, возращает произведение из 2*r и числа Pi 
    return 2 * math.pi * r

## Rectangle:



def area(a, b): 
- Функция принимает две стороны прямоугольника, возвращает его площадь
    return a * b 

def perimeter(a, b): 
- Функция принимает две стороны прямоугольника, возвращает его периметр`
    return 2*(a + b) 


## Square:

def area(a, b): 
- Принимает числа a и b, возвращает произведение a на b
    return a * b 

def perimeter(a, b): 
- Принимает числа a и b, возвращает произведение удвоенное a на b
    return 2*a + 2*b 


## Triangle:
''' python
def area(a):
 - Принимает число a, возращает квадрат a  
    return a * a


def perimeter(a):
 - Принимает число a, прозведение 4 на a  
    return 4 * a


# History with commits hashes:
commit 059bcc3ca4cff3652ca783d641f35b7e239eb56e (HEAD -> main, origin/main, origin/HEAD)
Author: rudik157 <144426377+rudik157@users.noreply.github.com>
Date:   Thu Sep 21 22:56:06 2023 +0300

    corrected mistake in rectangle.py

commit 05131862823049ac3d46fe698eb92122937b2d4a
Author: rudik157 <144426377+rudik157@users.noreply.github.com>
Date:   Thu Sep 21 22:42:13 2023 +0300

    new fail added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added