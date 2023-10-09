# Документация по geometric_lib
## Общее описание решения
geometric_lib представляет из себя библиотеку файлов, состоящих из функций, возвращающих по заданным параметрам некоторые характеристики геометрических фигур.  
__Настоящие файлы библиотеки:__
- square.py
- circle.py
- rectangle.py
- triangle.py

## Описание каждой функции с примерами вызова
### square.py
__area(a)__: принимает вещественное число a, возвращает площадь квадрата со стороной, равной a.  
area(1.0) = 1.0  
area(2.39) = 5.7121

__perimeter(a)__: принимает вещественное число a, возвращает периметр квадрата с стороной, равной a.  
perimeter(1.0) = 4.0  
perimeter(2.39) = 9.56

### circle.py
__area(r)__: принимает вещественное число r, возвращает площадь круга с радиусом, равным r.  
area(3.0) = 28.274333882308138  
area(2.39) = 17.94509139657026

__perimeter(r)__: принимает вещественное число r, возвращает периметр круга с радиусом, равным r.  
perimeter(3.0) = 18.84955592153876  
perimeter(2.39) = 15.016812884159211

### rectangle.py
__area(a, b)__: принимает вещественные числа a и b, возвращает площадь прямоугольника со сторонами, равными a и b.  
area(5.0, 6.0) = 30.0  
area(2.39, 2.23) = 5.3297

__perimeter(a)__: принимает вещественные числа a и b, возвращает периметр прямоугольника со сторонами, равными a и b.  
perimeter(5.0, 6.0) = 22.0  
perimeter(2.39, 2.23) = 9.24

### triangle.py
__area(a)__: принимает вещественное число a, возвращает площадь квадрата со стороной, равной a.  
area(23.0, 9.0) = 103.5  
area(5.5, 7.6) = 20.9

__perimeter(a)__: принимает вещественное число a, возвращает периметр квадрата co стороной, равной a.  
perimeter(23.0, 9.0, 17.0) = 49.0  
perimeter(5.5, 9.6, 7.6) = 22.7

## История изменения проекта с хешами комитов[^1]
commit 8ba9aeb3cea847b63a91ac378a2a6db758682460  
Author: smartiqa <info@smartiqa.ru>  
Date:   Thu, Mar 4, 2021

    L-03: Circle and square added
---
commit d078c8d9ee6155f3cb0e577d28d337b791de28e2  
Author: smartiqa <info@smartiqa.ru>  
Date:   Thu, Mar 4, 2021

    L-03: Docs added
---
commit 08ea7dc565836044b864e51857eb773c2dd6b608  
Author: Misha <misha.balakirsky@gmail.com>  
Date:   Tue, Sep 19, 2023

    Добавил файл для вычисления периметра прямоугольника
---
commit 9a128d41635e9eaf86897f8d7813f2f9c2aedfe1  
Author: Misha <misha.balakirsky@gmail.com>  
Date:   Tue, Sep 19, 2023

    Добавил файл для вычисления периметра треугольника
---
commit 8b4ca4c0fc0a7fe6e836de9cbe4662f933f54599  
Author: Misha <misha.balakirsky@gmail.com>  
Date:   Tue, Sep 19, 2023

    Исправлена ошибка в файле rectangle.py
---
commit 671f8f982c15fa7d3621de2308d6e5d90ccc65b1  
Author: Misha <misha.balakirsky@gmail.com>  
Date:   Sun, Oct 8, 2023

    Добавил комментарий к файлу square.py
---
commit 9076709fcd1b44519e5865e4690eb855bd1adcc0  
Author: Misha <misha.balakirsky@gmail.com>  
Date:   Sun, Oct 8, 2023

    Добавил комментарий к файлу circle.py
---
commit b9cd9ddec7373c06ae96e6c6285c0a1f6fac1921  
Author: Misha <misha.balakirsky@gmail.com>  
Date:   Sun, Oct 8, 2023

    Добавил комментарий к файлу rectangle.py
---
commit 6aa9023629a2422e1abfe6c6eb062468d175c119  
Author: Misha <misha.balakirsky@gmail.com>  
Date:   Sun, Oct 8, 2023

    Добавил комментарий к файлу triangle.py
---
commit a05eadb891c71af4b216d9f43c695632901e7fed  
Author: Misha <misha.balakirsky@gmail.com>  
Date:   Mon, Oct 9, 2023

    Поправил комментарий к triangle.py
---
commit 98b5861c1d0b603b57a2ee9f454d01500b26ea3b
Author: Misha <misha.balakirsky@gmail.com>
Date:   Mon, Oct 9, 2023

    Добавил примеры вызова функций к файлам

[^1]: в хронологическом порядке