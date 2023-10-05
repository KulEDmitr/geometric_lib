$\Large \color {#BCFF57} \sf Устройство\ функций$

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