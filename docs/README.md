# Geometric lib
## Math formulas and description of solution
The library counts area and perimeter of basic geometric shapes, such as circle, rectangle, triangle and square
The solution is based on simple geometric formulas such as:
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Usage examples and code

### Circle
has two methods: area and perimeter, that count area and perimeter using radius
```python
import circle
r = 3
P = circle.perimeter(r)
S = circle.area(r)
print("Perimeter is", P, "and area is", S) # prints perimeter and area of circle with radius 3
```

### Square
has two methods: area and perimeter, that count area and perimeter using length of side
```python
import square
a = 3 # length of side
P = square.perimeter(a)
S = square.area(a)
print("Perimeter is", P, "and area is", S) # prints perimeter and area of square with side 3
```

### Rectangle
has two methods: area and perimeter, that count area and perimeter using length of two sides
```python
import rectangle
a = 3 # length of the first side
b = 5 # length of the second side
P = rectangle.perimeter(a, b)
S = rectangle.area(a, b)
print("Perimeter is", P, "and area is", S) # prints perimeter and area of rectangle with sides 3 and 5
```

### Triangle
has two methods: area and perimeter, that count area and perimeter using length of side and height to this side
```python
import rectangle
a = 3 # length of the first side
h = 4 # length of the second side
P = rectangle.perimeter(a, h)
S = rectangle.area(a, h)
print("Perimeter is", P, "and area is", S) # prints perimeter and area of triangle with side 3 and height 4
```

## Development
the development had some significant commits. here are the most essential ones

- the first commit 8ba9aeb with circle and square
```
commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

diff --git a/circle.py b/circle.py
new file mode 100644
index 0000000..c3eb864
--- /dev/null
+++ b/circle.py
<...>
diff --git a/square.py b/square.py
new file mode 100644
index 0000000..0f98724
--- /dev/null
+++ b/square.py
```
- here are latest commits 3f7ccd3 and 843227f, adding the triangle and rectangle files
```
commit 3f7ccd34044bdb8eee446b02fc398ec9a41b5c5d
Author: Roriks <avanta.sae@gmail.com>
Date:   Mon Sep 4 20:44:43 2023 +0300

    created triangle.py to calculate triangle features

diff --git a/triangle.py b/triangle.py
new file mode 100644
index 0000000..2e1c3fd
--- /dev/null
+++ b/triangle.py
```

```
commit 843227ff295d9db78cf82aa678aa9e161f3e5ec8
Author: Roriks <avanta.sae@gmail.com>
Date:   Mon Sep 4 20:45:56 2023 +0300

    created rectangle.py to calculate rectangle features

diff --git a/rectangle.py b/rectangle.py
new file mode 100644
index 0000000..c77ece6
--- /dev/null
+++ b/rectangle.py
```