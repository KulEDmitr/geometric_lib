# Математические формулы
## Площадь
- Окружность: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²

## Периметр
- Окружность: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a


# Документация к библиотеке Geometric_lib
## Модуль [circle.py](../circle.py)
- def area(r):
    ```
    Принимает число r(float), возвращает площадь окружности с радиусом r
    ```
    return math.pi * r * r
    ```
    Примеры вызова
    ```
    area(1) #3.1415926536

- def perimeter(r):
    ```
    Принимает число r(float), возвращает длину окружности с радиусом r
    ```
    return 2 * math.pi * r
    ```
    Примеры вызова:
    ```
    area(1) #6.2831853072

## Модуль [rectangle.py](../rectangle.py)
- def area(a, b): 
    ```
    Возвращает площадь прямоугольника

        Параметры:
                a(float): длина первой стороны прямоугольника
                b(float): длина воторой стороны прямоугольника
        Возвращает значение:
                a * b(float): площадь прямоугольника со сторонами a и b
    ```
    return a * b
    ```
    Примеры вызова
    ```
    area(1, 2) #2

- def perimeter(a, b): 
    ```
    Возвращает периметр прямоугольника

        Параметры:
                a(float): длина первой стороны прямоугольника
                b(float): длина воторой стороны прямоугольника
        Возвращает значение:
                a * b(float): периметр прямоугольника со сторонами a и b
    ```
    return 2 * a + 2 * b 
     ```
    Примеры вызова
    ```
    area(1, 2) #6

## Модуль [square.py](../square.py)

- def area(a):
    ```
    Принимает число a(float), возвращает площадь квадрата со сторонами a
    ```
    return a * a
     ```
    Примеры вызова
    ```
    area(1) #1


- def perimeter(a):
    ```
    Принимает число a(float), возвращает периметр квадрата со сторонами a
    ```
    return 4 * a
     ```
    Примеры вызова
    ```
    area(1) #4

## Модуль [triangle.py](../triangle.py)
- def area(a, h): 
    ```
    Возвращает площадь треугольника

        Параметры:
                a(float): длина стороны треугольника к которой проведена высота
                h(float): длина высоты треугольника которая проведена к сотроне 
        Возвращает значение:
                a * h(float): площадь треугольника со стороной a и высотой h
    ```
    return a * h / 2 
     ```
    Примеры вызова
    ```
    area(2, 1) #1

- def perimeter(a, b, c): 
    ```
    Возвращает периметр треугольника

        Параметры:
                a(float): длина первой стороны треугольника
                b(float): длина воторой стороны треугольника
                c(float): длина третьей стороны треугольника
        Возвращает значение:
                a + b + с(float): периметр треугольника со сторонами a, b и c
    ```
    return a + b + c
     ```
    Примеры вызова
    ```
    area(2, 3, 4) #9

## История изменения проекта с хешами комитов
```bash
commit 6872a5ce02b9d13a7d0c7358b5107fe90ac91eea (HEAD -> new_features_465453, origin/new_features_465453)
Author: EmiliyaV <emiliyapolomina456@gmail.com>
Date:   Tue Oct 8 17:46:10 2024 +0300

    fixed mistake in rectangle.py and added triangle.py
```
```diff
--git a/triangle.py b/triangle.py
new file mode 100644
index 0000000..38f9701
--- /dev/null
+++ b/triangle.py
@@ -0,0 +1,6 @@
+def area(a, h):
+    return a * h / 2
+
+def perimeter(a, b, c):
+    return a + b + c
+
```
```bash
commit 1fe26997305296b483b9edd0ceec8e67419e7e04
Author: EmiliyaV <emiliyapolomina456@gmail.com>
Date:   Tue Oct 8 17:37:00 2024 +0300
:
commit 6872a5ce02b9d13a7d0c7358b5107fe90ac91eea (HEAD -> new_features_465453, origin/new_features_465453)
Author: EmiliyaV <emiliyapolomina456@gmail.com>
Date:   Tue Oct 8 17:46:10 2024 +0300

    fixed mistake in rectangle.py and added triangle.py
```
```diff
--git a/triangle.py b/triangle.py
new file mode 100644
index 0000000..38f9701
--- /dev/null
+++ b/triangle.py
@@ -0,0 +1,6 @@
+def area(a, h):
+    return a * h / 2
+
+def perimeter(a, b, c):
+    return a + b + c
+
```
```bash
commit 1fe26997305296b483b9edd0ceec8e67419e7e04
Author: EmiliyaV <emiliyapolomina456@gmail.com>
Date:   Tue Oct 8 17:37:00 2024 +0300
:
commit 6872a5ce02b9d13a7d0c7358b5107fe90ac91eea (HEAD -> new_features_465453, origin/new_features_465453)
Author: EmiliyaV <emiliyapolomina456@gmail.com>
Date:   Tue Oct 8 17:46:10 2024 +0300

    fixed mistake in rectangle.py and added triangle.py
```
```diff
--git a/triangle.py b/triangle.py
new file mode 100644
index 0000000..38f9701
--- /dev/null
+++ b/triangle.py
@@ -0,0 +1,6 @@
+def area(a, h):
+    return a * h / 2
+
+def perimeter(a, b, c):
+    return a + b + c
+
```
```bash
commit 1fe26997305296b483b9edd0ceec8e67419e7e04
Author: EmiliyaV <emiliyapolomina456@gmail.com>
Date:   Tue Oct 8 17:37:00 2024 +0300
:
commit 6872a5ce02b9d13a7d0c7358b5107fe90ac91eea (HEAD -> new_features_465453, origin/new_features_465453)
Author: EmiliyaV <emiliyapolomina456@gmail.com>
Date:   Tue Oct 8 17:46:10 2024 +0300

    fixed mistake in rectangle.py and added triangle.py
```
```diff
--git a/triangle.py b/triangle.py
new file mode 100644
index 0000000..38f9701
--- /dev/null
+++ b/triangle.py
@@ -0,0 +1,6 @@
+def area(a, h):
+    return a * h / 2
+
+def perimeter(a, b, c):
+    return a + b + c
+
```
```bash
commit 1fe26997305296b483b9edd0ceec8e67419e7e04
Author: EmiliyaV <emiliyapolomina456@gmail.com>
Date:   Tue Oct 8 17:37:00 2024 +0300
```
