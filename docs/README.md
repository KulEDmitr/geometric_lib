# Math
Project contains modules for finding area and perimeter of geometry figures

## Modules
### circle.py
1. ```area(r: float) -> float```
   - Returns area of the circle with given radius
   - Example: 
   ```
   print(area(1.0))
   # output: 3.1415926
   
   print(area(0))
   # output: 0.0
   ```
   
1. ```perimeter(r: float) -> float```
   - Returns primeter of the circle with given radius
   - Example: 
   ```
   print(perimeter(0.5))
   # output: 3.1415926
   
   print(perimeter(0))
   # output: 0.0
   ```
### rectangle.py
1. ```area(a: float, b: float) -> float```
   - Returns area of the rectangle with given sides
   - Example: 
   ```
   print(area(1.0, 3.5))
   # output: 3.5
   
   print(area(32, 0.25))
   # output: 8.0
   ```
   
1. ```perimeter(a: float, b: float) -> float```
   - Returns perimeter of the rectangle with given sides
   - Example: 
   ```
   print(perimeter(1.0, 3.5))
   # output: 9.0
   
   print(perimeter(32, 1))
   # output: 66
   ```
   
### square.py
1. ```area(a: float) -> float```
   - Returns area of the square with given side
   - Example: 
   ```
   print(area(1.0))
   # output: 1.0
   
   print(area(1.1))
   # output: 1.21
   ```
   
1. ```perimeter(a: float) -> float```
   - Returns perimeter of the square with given side
   - Example: 
   ```
   print(perimeter(0.5))
   # output: 2.0
   
   print(perimeter(59.75))
   # output: 239.0
   ```
   
### triangle.py
1. ```area(a: float, h: float) -> float```
   - Returns area of the triangle with given side and height drawn to this side
   - Example: 
   ```
   print(area(1.0, 4))
   # output: 2.0
   
   print(area(100, 2))
   # output: 100
   ```
   
1. ```perimeter(a: float, b: float, c: float) -> float```
   - Returns area of the triangle with three given sides
   - Example: 
   ```
   print(perimeter(3, 4, 5))
   # output: 12
   
   print(perimeter(11.9, 12.1, 10.2))
   # output: 34.2
   ```
   
## Commits
* **65d37149: danyarmarkin**  fix bug with rect perimeter
* **ee837feb: danyarmarkin**  add new file rectangle.py
* **d078c8d9: smartiqa** L-03: Docs added
* **8ba9aeb3: smartiqa** L-03: Circle and square added

## Testing
Modules tested with *unittest*. Testing cases:
1. Null numbers
1. Big numbers
1. Float numbers
1. Not-normal input data (ex. str)