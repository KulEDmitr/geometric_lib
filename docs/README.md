# <a id="main" href="https://github.com/franchescooo/geometric_lib"> geometriclib </a>

### <a id="content"> Содержание </a>
- [Основная информация](#info)
- [Примеры использования](#using)
- [Реализация](#realisation)
  - [circle.py](#realisation-circle)
  - [square.py](#realisation-square)
  - [rectangle.py](#realisation-rectangle)
  - [triangle.py](#realisation-triangle)
- [Математика](#math)
- [История](#history)
- [Ресурсы](#sources)

    
## <a id="info"> Основная информация </a>
$\quad \large \color {#FFB1F9} \sf {\Large \color {#BCFF57} geometriclib}\ -\ Пользовательская\ библиотека\ для\ работы\ с\ евклидовой\ геометрией$

$\quad \large \color {#FFB1F9} \sf Позволяет\ упростить\ работу\ с\ площадью\ и\ периметром\ базовых\ геометрических\ фигур$

$\quad \large \color {#FFB1F9} \sf Разработана \quad$ <a href="https://github.com/franchescooo"> **Артурчиком из M3102** </a>


## <a id="using" href="https://github.com/franchescooo/geometric_lib/blob/main/docs/USING.md"> Использование </a> 

$\Huge \color {#BCFF57} \bf Quick Start$

$\large \color {#FFB1F9} \sf Клонируйте\ этот\ репозиторий\ в\ свой\ проект$
```
cd project/path/
git clone https://github.com/franchescooo/geometric_lib.git
```

$\large \color {#FFB1F9} \sf В\ любом\ python\ файле\ импортируйте\ библиотеку\ и наслаждайтесь$
```py
import geometric_lib.circle as circle, geometric_lib.square as square

print(circle.perimeter(10)) # 62.83185307179586
print(square.area(10)) # 100 
```

## <a id="realisation" href="https://github.com/franchescooo/geometric_lib/blob/main/docs/FUNCTIONS.md"> Реализация </a>
### <a id="realisation-circle" href="https://github.com/franchescooo/geometric_lib/blob/main/circle.py"> circle.py </a>
```py
import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r
```

### <a id="realisation-square" href="https://github.com/franchescooo/geometric_lib/blob/main/square.py"> square.py </a>
```py
def area(a):
    return a * a

def perimeter(a):
    return 4 * a
```

### <a id="realisation-rectangle" href="https://github.com/franchescooo/geometric_lib/blob/main/rectangle.py"> rectangle.py </a>
```py
def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)
```

### <a id="realisation-triangle" href="https://github.com/franchescooo/geometric_lib/blob/main/triangle.py"> triangle.py </a>
```py
def area(a, h): 
    return a * h / 2

def perimeter(a, b, c): 
    return a + b + c 
```

## <a id="tests" href="https://github.com/franchescooo/geometric_lib/blob/main/docs/TESTS.md"> Проведенные тесты </a>
|                  Компонента                 |                Результаты тестирования                  |
| ------------------------------------------- | :-----------------------------------------------------: |
| $\color {#FFB1F9} \normalsize \sf circle$   | $\quad \color {#F5D033} \bf 50\%$                       |
| $\color {#FFB1F9} \normalsize \sf rectangle$| $\quad \color {#92000A} \bf Тестирование\ не\ проведено$|
| $\color {#FFB1F9} \normalsize \sf square$   | $\quad \color {#92000A} \bf Тестирование\ не\ проведено$|
| $\color {#FFB1F9} \normalsize \sf triangle$ | $\quad \color {#92000A} \bf Тестирование\ не\ проведено$|

## <a id="math" href="https://github.com/franchescooo/geometric_lib/blob/main/docs/MATHFORMULS.md"> Математика </a>
$\large \color {#BCFF57} \sf Площадь$
|                    Фигура                         |                         Формула                            |
| ------------------------------------------------- | :--------------------------------------------------------: |
| $\color {#FFB1F9} \normalsize \sf Круг$           | $\quad \color {#FAED5A} S = \pi r²$                        |
| $\color {#FFB1F9} \normalsize \sf Квадрат$        | $\quad \color {#FAED5A} S = \int_0^a a \mathrm{d}x = a^2$  |
| $\color {#FFB1F9} \normalsize \sf Треугольник$    | $\quad \color {#FAED5A} S = \frac{ah}{2}$                  |
| $\color {#FFB1F9} \normalsize \sf Прямоугольник$  | $\quad \color {#FAED5A} S = ab$                            |

$\large \color {#BCFF57} \sf Периметр$
|                    Фигура                         |                         Формула                            |
| ------------------------------------------------- | :--------------------------------------------------------: |
| $\color {#FFB1F9} \normalsize \sf Круг$           | $\quad \color {#FAED5A} P = 2πr$                           |
| $\color {#FFB1F9} \normalsize \sf Квадрат$        | $\quad \color {#FAED5A} P = 4a$                            |
| $\color {#FFB1F9} \normalsize \sf Треугольник$    | $\quad \color {#FAED5A} P = a + b + c$                     |
| $\color {#FFB1F9} \normalsize \sf Прямоугольник$  | $\quad \color {#FAED5A} P = 2a + 2b$                       |

## <a id="history" href="https://github.com/franchescooo/geometric_lib/blob/main/docs/HISTORY.md"> История </a>
```
commit b530613d38f76530c7e57f6afd23599bf740a939
Date:   Mon Sep 11 22:23:14 2023 +0300
    Triangle area and perimeter calculating added. Rectangle perimeter formula fixed.

commit 01dd1c4c6419dee1205f6a54eb548ab56bcf04a1
Date:   Mon Sep 11 22:21:06 2023 +0300
    Rectangle added
```

## <a id="sources"> Ресурсы </a>

$\large \color {#BCFF57} \sf Гайд\ по\ \LaTeX$

https://katex.org/

$\large \color {#BCFF57} \sf Первоначальные\ прототипы\ geometriclib$

https://github.com/smartiqaorg/geometric_lib

https://github.com/RuslanKoynov/geometric_lib

https://github.com/KulEDmitr/geometric_lib

$\large \color {#BCFF57} \sf Математика\ -\ народный\ фольклор$
