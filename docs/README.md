
# Solution
## Library for calculating geometric data
## Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Project description:

## File circle.py contains 2 formulas:
- Function **area(r)** that calculates area of circle with radius **r**
  - Example:
  > r = 5
  > 
  > s = area(r)
  > 
  > print(s)
  - Output:
  > 78.5398163
- Function **permimeter(r)** that calculates perimiter of circle with radius **r**
  - Example:
  > r = 5
  > 
  > p = perimeter(r)
  > 
  > print(p)
  - Output:
  > 31.4159265

## File rectangle.py contains 2 formulas:
- Function **area(a, b)** that calculates area of rectangle with sides **a** and **b**
  - Example:
  > a, b = 2, 3
  > 
  > s = area(a, b)
  > 
  > print(s)
  - Output:
  > 6
- Function **perimeter(a, b)** that calculates perimeter of rectangle with sides **a** and **b**
  - Example:
  > a, b = 2, 3
  > 
  > p = perimeter(a, b)
  > 
  > print(p)
  - Output:
  > 10

## File square.py contains 2 formulas:
- Function **area(a)** that calculates area of square with side **a**
  - Example:
  > a = 5
  > 
  > s = area(a)
  > 
  > print(s)
  - Output:
  > 25
- Function **perimeter(a)** that calculates perimeter of square with side **a**
  - Example:
  > a = 5
  > 
  > p = perimeter(a)
  > 
  > print(p)
  - Output:
  > 20

## File triangle.py contains 2 formulas:
- Function **area(a, h)** that calculates area of triangle with side **a** and height **h** that was drawn to the side **a**
  - Example:
  > a, h = 5, 3
  > 
  > s = area(a, h)
  > 
  > print(s)
  - Output:
  > 7.5
- Function **perimeter(a, h)** that calculates perimeter of triangle with side **a** and height **h** that was drawn to the side **a**
  - Example:
  > a, b, c = 3, 4, 5
  > 
  > p = perimeter(a, b, c)
  > 
  > print(p)
  - Output:
  > 12

# Project history
1. Circle.py and square.py added
   - **Commit message**: "L-03: Circle and square added"
   - **Hash**: 8ba9aeb
1. Docs folder created
   - **Commit message**: "L-03: Docs added"
   - **Hash**: d078c8d
1. Branch "new_features" created, rectangle.py added
   - **Commit message**: "rectangle added"
   - **Hash**: 81ba85b
1. File triangle.py added and error in rectangle.py got fixed
   - **Commit message**: "triangle added + rectangle fixed"
   - **Hash**: ce10616
1. Created new branch for unittests and pulled all files in a separate directory
   - **Commit message**: "pulled library in a separate directory and added unittest tests"
   - **Hash**: 0ad78c4
1. Merged unittest's branch with main
   - **Commit message**: "merged unittest_branch and updated docs"
   - **Hash**: 69112b9