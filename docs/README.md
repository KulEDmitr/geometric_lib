# Общее описание репозитория
Репозиторий содержит файлы для расчёта периметра и площади для следующих геометрических фигур: круг, треугольник, квадрат, прямоугольник. Каждой фигуре соответствует файл с её названием, в котором находятся соответствующие функции. Также в репозитории есть файл для нахождения результатов совершения над 2 числами следущих арифметических операций: сложение, умножение.


# Описание каждой функции с примерами вызова
## Файл **actions.py** (*арифметические операции*)
### (int) F_sum( (int) a, (int) b)
Возвращает сумму чисел a и b

* Параметры:
	- **a** (int)*: первое число*
	- **b** (int)*: второе число*
		
* Возвращаемое значение:
	- (int): **сумма чисел**

* Пример вызова:
	- `F_sum(3, 2) # 5`

### (int) F_mult( (int) a, (int) b)
Возвращает произведение чисел a и b

* Параметры:
	- **a** (int)*: первое число*
	- **b** (int)*: второе число*
		
* Возвращаемое значение:
	- (int): **произведение чисел**

* Пример вызова:
	- `F_mult(3, 2) # 6`
	

## Файл **circle.py** (*круг*)
### (float) area( (int) r)
Возвращает площадь круга с радиусом r.
	
* Параметры:
	- **r** (int)*: длина радиуса круга*
		
* Возвращаемое значение:
	- (float): **площадь круга**

* Пример вызова:
	- `area(3) # 28.274333882308138`

### (float) perimeter( (int) r)
Возвращает периметр круга с радиусом r.
	
* Параметры:
	- **r** (int)*: длина радиуса круга*
		
* Возвращаемое значение:
	- (float): периметр круга

* Пример вызова:
	- `perimeter(3) # 18.84955592153876`


## Файл **rectangle.py** (*прямоугольник*)
### (int) area( (int) a, (int) b)
Возвращает площадь прямоугольника со сторонами a и b

* Параметры:
	- **a** (int)*: длина прямоугольника*
	- **b** (int)*: ширина прямоугольника*
		
* Возвращаемое значение:
	- (int): **площадь прямоугольника**

* Пример вызова:
	- `area(3, 2) # 6`

### (int) perimeter( (int) a, (int) b)
Возвращает периметр прямоугольника со сторонами a и b

* Параметры:
	- **a** (int)*: длина прямоугольника*
	- **b** (int)*: ширина прямоугольника*
		
* Возвращаемое значение:
	- (int): **периметр прямоугольника**

* Пример вызова:
	- `perimeter(3, 2) # 10`


## Файл **square.py** (*квадрат*)
### (int) area( (int) a)
Возвращает площадь квадрата со стороной a

* Параметры:
	- **a** (int)*: длина стороны квадрата*
		
* Возвращаемое значение:
	- (int): **площадь квадрата**

* Пример вызова:
	- `area(3) # 9`

### (int) perimeter( (int) a)
Возвращает периметр квадрата со стороной a

* Параметры:
	- **a** (int)*: длина стороны квадрата*
		
* Возвращаемое значение:
	- (int): **периметр квадрата**

* Пример вызова:
	- `area(3) # 12`


## Файл **triangle.py** (*треугольник*)
### (float) area( (int) a, (int) h)
Возвращает площадь треугольника с высотой длиной h, опущенной к стороне длиной a.
	
* Параметры:
	- **a** (int)*: длина стороны треугольника*
	- **h** (int)*: длина высоты треугольника*

* Возвращаемое значение:
	- (float): **площадь треугольника**

* Пример вызова:
	- `area(3, 2) # 3.0`

### (int) perimeter( (int) a, (int) b, (int) c)
Возвращает периметр треугольника со сторонами a, b и с

* Параметры:
	- **a** (int)*: длина первой стороны треугольника*
	- **b** (int)*: длина второй стороны треугольника*
	- **c** (int)*: длина третьей стороны треугольника*
		
* Возвращаемое значение:
	- (int): **периметр треугольника**

* Пример вызова:
	- `perimeter(3, 2, 4) # 9`


# История изменения проекта с хешами комитов

commit d3970973bcfe0e8b57740e420f97bf327947c16c (HEAD -> main)
Author: nikita <nkarbofos@gmail.com>
Date:   Sun Oct 8 09:17:44 2023 +0300

    declarations fixed

commit dedf52d0d81e788592451d29ff2210680bfd05af
Author: nikita <nkarbofos@gmail.com>
Date:   Sun Oct 8 08:44:45 2023 +0300

    square.py fixed

commit b9602d6e2f44ee3e85e20fc66111e2079aed8ef5
Author: nikita <nkarbofos@gmail.com>
Date:   Sun Oct 8 08:41:20 2023 +0300

    actions.py fixed

commit 979a638337efb51a8bd9b3365e411d1c9b814f74
Author: nikita <nkarbofos@gmail.com>
Date:   Thu Oct 5 21:39:08 2023 +0300

    documentation made

commit 30bc50f945de74ec2985fab0eeb9911d76376e44
Author: nikita <nkarbofos@gmail.com>
Date:   Thu Oct 5 13:19:48 2023 +0300

    circle, triangle fixed

commit 2b6f1d2cb3df221b4aeba6295a242cde829ba3e8
Author: nikita <nkarbofos@gmail.com>
Date:   Wed Oct 4 21:33:42 2023 +0300

    functions declared

commit 96589d8baa84f8e97bc76ab4f00fa754da52f6cc
Merge: 4cda39f fd08fd0
Author: nikita <nkarbofos@gmail.com>
Date:   Thu Sep 7 18:23:50 2023 +0300

    Merge branch 'new_features_409126'

commit fd08fd05800ec90df7e70d2cc8c27630358d93e2 (new_features_409126)
Author: nikita <nkarbofos@gmail.com>
Date:   Thu Sep 7 17:58:16 2023 +0300

    actions.py fixed F_mult

commit a4018e9a7d1fb8e3f24c7144f44cff31cc3b2430
Author: nikita <nkarbofos@gmail.com>
Date:   Thu Sep 7 17:55:58 2023 +0300

    actions.py added

commit 4cda39fdb9267e34f4777a840dc12046341ef34c
Author: nikita <nkarbofos@gmail.com>
Date:   Thu Sep 7 17:29:25 2023 +0300

    fixed perimeter in rectangle.py

commit 665630d2f420ab2a4130abe776edd6ea1f6c6081
Author: nikita <nkarbofos@gmail.com>
Date:   Thu Sep 7 17:24:28 2023 +0300

    added triangle.py

commit d1067d6148ae981ac3402a363c2dbb2c9f512bf9
Author: nikita <nkarbofos@gmail.com>
Date:   Thu Sep 7 17:16:33 2023 +0300

    added rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added


# Другое
## Математические формулы
### Площаль
- Круг: S = πR²
- Треугольник: S = ab
- Квадрат: S = a²

### Периметр
- Круг: P = 2πR
- Треугольник: P = 2a + 2b
- Квадрат: P = 4a
