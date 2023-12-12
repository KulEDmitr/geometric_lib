# Repository with .py files for counting areas and perimiters of triangle, square and rectangle

## Documentation is an integral part of any IT product and we will enrich our project with it both with separate documentation and implement it into the source code.
1. Each declaration of a function in the project files should begin with a comment block that describes the function itself and an example of its call.\
2. The docs directory should appear in the project structure, which should contain documentation on the project written in markdown notation (read more about it here), which includes the following sections:\
- general description of the solution 
- description of each function with call examples
- project modification history with commit hashes (except for the last entry)

## Math formulas, used in files:
### Area
- Circle: S = πR²
- Triangle: S = ah/2
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Triangle: P = a + b + c
- Rectangle: P = 2a + 2b
- Square: P = 4a

## General description of the solution:

### Files situated in the repository:
- rectangle.py
- triangle.py
- square.py
- circle.py
- \docs\README.md

## Functions' descriptions:

## rectangle.py

### Area:
Takes the numbers a and b, returns their product\
Parameters:\
- a (int, float, etc...) first number
- b (int, float, etc...) the second number
Return value:\
- a_b_multiplied (int, float, etc...) product of numbers a and b
Example of a function call:\
- input >> 2, 3
- output << 6

### Perimeter:
Takes the numbers a and b, returns their doubled sum\
Parameters:\
- a (int, float, etc...) first number
- b (int, float, etc...) the second number
Return value:\
- a_b_summa_doubled (int, float, etc...) the doubled sum of the numbers a and b
Example of a function call:\
- input >> 2, 3
- output << 10

## square.py

### Area:
Takes a number n, returns its square\
Parameters:\
- a (int, float, etc...) number
Return value:\
- a_squared (int, float, etc...) the square of the number a
Example of a function call:\
- input >> 2
- output << 4

### Perimeter:
Takes the number n, returns it multiplied by 4\
Parameters:\
- a (int, float, etc...) number
Return value:\
- a_multiplied_by_4 (int, float, etc...) the number a multiplied by 4
Example of a function call:\
- input >> 2
- output << 8

## triangle.py

### Area:
Accepts the numbers a and h, returns their semi-reproduction\
Parameters:\
- a (int, float, etc...) the first number
- h (int, float, etc...) the second number
Return value:\
- a_h_multiplied_half (int, float, etc...) semi-reproduction of numbers a and h
Example of a function call:\
- input >> 2, 3
- output << 3

### Perimeter:
Accepts the numbers a b and c, returns their sum\
Parameters:\
- a (int, float, etc...) first number
- b (int, float, etc...) the second number
- c (int, float, etc...) the third number
Return value:\
- a_b_c_summ (int, float, etc...) sum of numbers a,b,c
Example of a function call:\
- input >> 3, 4, 5
- output << 12

## circle.py

### Area:
*import the math library to get the number pi\
Takes the number r, returns its square multiplied by pi\
Parameters:\
- r (int, float, etc...) first number
Return value:\
- a_squres_multiplied_by_pi (float, etc...) the square of the number r multiplied by the number pi
Example of a function call:\
- input >> 3
- output << 28.274333882308138

### Perimeter:
*import the math library to get the number pi\
Takes the number r, returns it multiplied by twice the number pi\
Parameters:\
- r (int, float, etc...) first number
Return value:\
- a_multiplied_by_double_pi (float, etc...) the number r multiplied by twice the number pi
Example of a function call:\
- input >> 2
- output << 12.566370614359172

## Git commits hashes:
- commit 226288e0efeca62cd658beed94c6031031fdb8dc (HEAD -> labwork2)\
Author: Alexander Kim <limosha@inbox.ru>\
Date:   Sat Oct 7 09:57:29 2023 +0300\

    modified 4 .py files

- commit 69e6f4c1fdaf8c880be2eddf306d1866a32ad187 (origin/new_features_391091, origin/main, origin/HEAD)\
Author: Alexander Kim <limosha@inbox.ru>\
Date:   Tue Sep 19 14:05:34 2023 +0300\

    mistake in rectangle.py was fixed

- commit e46bba849a8e8a20002517f1fc95517f0ebedbd8\
Author: Alexander Kim <limosha@inbox.ru>\
Date:   Tue Sep 19 13:59:01 2023 +0300\

    second file was added

- commit bad1e46e80ed1cb428a30286f8db7e4ae7947114\
Author: Alexander Kim <limosha@inbox.ru>\
Date:   Tue Sep 19 13:55:22 2023 +0300\

    new file was added

- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2\
Author: smartiqa <info@smartiqa.ru>\
Date:   Thu Mar 4 14:55:29 2021 +0300\

    L-03: Docs added

- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460\
Author: smartiqa <info@smartiqa.ru>\
Date:   Thu Mar 4 14:54:08 2021 +0300\

    L-03: Circle and square added

## Additional info:

This documentation was modified using [Visual Studio Code](https://code.visualstudio.com/).

> [!NOTE]
> This file stores the history of changes to the project with the hashes of the comits except the last one.
