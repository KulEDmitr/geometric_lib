# Documentation
В этом проекте находятся файлы ```.py``` с названиями математических фигур.
Пример: ```circle.py```.

В этих файлах релиализованы функции для нахождения периметра и площади различных геометрических фигур.
## Math formulas
### Area
- Circle: S = π * R²
- Rectangle: S = a * b
- Square: S = a²
- Triangle: S = a * h / 2  

### Perimeter
- Circle: P = 2 * π * R
- Rectangle: P = 2 * (a + b)
- Square: P = 4 * a
- Triangle: P = a + b + c
## Functions
### circle.py
В этом файле реализованы функции для нахождения периметра и площади круга.

**_Area function_**
```
def area(r):
    return math.pi * r * r
``` 
Вызов функции
```print(area(2.0))```

выведет в командную строку _12.56_.

**_Perimeter fucntion_**
```
def perimeter(r):
    return 2 * math.pi * r
```
Вызов функции
```print(perimeter(2.5))``` 

вывыдет в командную строку _15.7_.

### rectangle.py
В этом файле реализованы функции для нахождения периметра и площади прямоугольника.

**_Area function_**
```
def area(a, b): 
    return a * b
```
Вызов функции
 ```print(area(2.0, 3.5))```

выведет в командную строку _7.0_.

**_Perimeter function_**
```
def perimeter(a, b):
    return 2 * (a + b)
```
Вызов функции
```print(perimeter(2.0, 3.5))```

Выведет в командную строку _11.0_.

### square.py
В этом файле реализованы функции для нахождения периметра и площади квадрата.

**_Area function_**
```
def area(a):
    return a * a
```
Вызов функции
```print(area(3.0))```

выведет в командную строку _9.0_.

**_Perimeter fucntion_**
```
def perimeter(a):
    return 4 * a
```
Вызов функции
```print(perimeter(3.0))```

выведет в командную строку _12.0_.

### triangle.py
В этом файле реализованы функции для нахождения периметра и площади треугольника.

**_Area function_**
```
def area(a, h): 
    return a * h / 2 
```
Вызов функции
```print(area(3.0, 10.0))```

выведет в командную строку _15.0_.

**_Perimeter function_**
```
def perimeter(a, b, c): 
    return a + b + c
```
Вызов функции
```print(perimeter(3.0, 10.0, 5.5))```

выведет в командную строку _18.5_.

## History of commits
```
* commit 9adc9acc7c0d4769cd215942f7d798ec5d14364f (HEAD -> documentation)
| Author: deknospe <deknospe@gmail.com>
| Date:   Thu Oct 17 19:26:04 2024 +0300
| 
|     Add description to functions
|
* commit 039af87dabcb8fb6be9b5db176b8a627753621cf (origin/new_features_465663, new_features_465663)
| Author: deknospe <deknospe@gmail.com>
| Date:   Thu Oct 3 23:39:02 2024 +0300
|
|     Fix mistake in rectangle.py
|
|     Add description to functions
|
* commit 039af87dabcb8fb6be9b5db176b8a627753621cf (origin/new_features_465663, new_features_465663)
| Author: deknospe <deknospe@gmail.com>
| Date:   Thu Oct 3 23:39:02 2024 +0300
|
|     Fix mistake in rectangle.py
|
* commit 07a9b861ac745362a5549e04f7b92127455a2c44
| Author: deknospe <deknospe@gmail.com>
| Date:   Thu Oct 3 23:38:32 2024 +0300
|
|     Add triangle.py
|
* commit a79ba8d0c4e36078a0dc9645697c283a0954bcfa
| Author: deknospe <deknospe@gmail.com>
| Date:   Thu Oct 3 23:33:18 2024 +0300
|
|     Add rectangle.py
|
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
| Author: smartiqa <info@smartiqa.ru>
| Date:   Thu Mar 4 14:55:29 2021 +0300
|
|     L-03: Docs added
|
* commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:54:08 2021 +0300

      L-03: Circle and square added
```
