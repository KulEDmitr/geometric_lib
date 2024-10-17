# Лабораторная работа 2
## Общее описание решения
В каждой программе описано по две функции. Функция нахождения площади и функция нахождения периметра. 
Всего в проекте четыре программы "circle.py", "rectangle.py", "square.py", "traingle.py" для нахождения площадей круга, прямоугольника, квадрата и треугольника соответственно.
## Описание каждой функции с примерами вызова
### circle.py
def area(r):
    return math.pi * r * r
    '''
    Принимает число r, возвращает площадь окружности с радиусом r.
    
    Напрмер:
        Вход: 6
        Выход: 113.09733552923255
    '''

def perimeter(r):
    return 2 * math.pi * r
    '''
    Принимает число r, возвращает периметр окружности с радиусом r.
    
    Напрмер:
        Вход: 4
        Выход: 25.132741228718345
    '''
### rectangle.py
def area(a, b): 
    return a * b 
    '''
    Принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b.
    
    Напрмер:
        Вход: 8
              3
        Выход: 24
    '''

def perimeter(a, b): 
    return (a + b) * 2
    '''
    Принимает числа a и b, возвращает периметр со сторонами a и b.
    
    Напрмер:
        Вход: 4
              7
        Выход: 22
    '''
### square.py
def area(a):
    return a * a
    '''
    Принимает число a, возвращает площадь квадрата со сторонами a.
    
    Напрмер:
        Вход: 72
        Выход: 5184
    '''

def perimeter(a):
    return 4 * a
    '''
    Принимает число a, возвращает периметр квадрата со сторонами a.
    
    Напрмер:
        Вход: 23
        Выход: 92
    '''
### traingle.py
def area(a, h): 
    return a * h / 2 
    '''
    Принимает числа a и h, возвращает площадь треугольника со стороной a и высотой h.
    
    Напрмер:
        Вход: 7
              2
        Выход: 7.0
    '''

def perimeter(a, b, c): 
    return a + b + c 
    '''
    Принимает числа a и h, возвращает периметр треугольника со сторонами a, b и c.
    
    Напрмер:
        Вход: 9
              14
              6
        Выход: 29
    '''
## История изменения проекта с хешами комитов
commit 0fb0daf790749fed7962725e91783d09788096d2 (HEAD -> laba2, origin/new_features_465330, new_features_465330)
Author: doastoi <bykova.elizaveta3939@gmail.com>
Date:   Thu Oct 3 22:24:21 2024 +0300

    "added new file "traingle.py", fixed a bug in "rectangle.py"."

commit 7f21cd77f88424b97ebd21b227ce8a9695fd72f1
Author: doastoi <bykova.elizaveta3939@gmail.com>
Date:   Thu Oct 3 22:20:26 2024 +0300

    "added new file "rectangle.py"."

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300
