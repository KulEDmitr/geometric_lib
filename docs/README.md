# Geometric library
## General description
**This library presents basic functions to find such geometric parameters as area and perimeter. Each shape has its own file.py with _area and perimeter functions_**
## Functions
```python
def area(params):
    params: shape's params
    return value: area of a shape
```
```python
def perimeter(params):
    params: shape's params
    return value: perimeter of a shape
```
### Circle
```python
def area(r):
    '''
    Parameter: r (int): circle radius
    Return value: area of a circle with radius r
    '''
def perimeter(r):
    '''
    Parameter: r (int): circle radius
    Return value: perimeter of a circle with radius r
    '''

area(3) #returns 28.26
perimeter(3) #returns 18.84
```
### Rectangle
```python
def area(a, b): 
    '''
    Parameter: a (int): first integer number
    Parameter: b (int): second integer number
    Return value: area of rectangle with sides a and b
    '''
def perimeter(a, b): 
    '''
    Parameter: a (int): first integer number
    Parameter: b (int): second integer number
    Return value: perimeter of rectangle with sides a and b
    '''

area(3, 4) #returns 12
perimeter(3, 4) #returns 14
```
### Square
```python
def area(a): 
    '''
    Parameter: a (int): integer number
    Return value: area of square with side a
    '''
def perimeter(a): 
    '''
    Parameter: a (int): integer number
    Return value: area of square with side a
    '''
    
area(3) #returns 9
perimeter(3) #returns 12
```
### Triangle
```python
def area(a, h):
'''
    Parameter: a (int): first integer number
    Parameter: h (int): second integer number
    Return value: area of triangle with side a and height h
'''
def perimeter(a, b, c):
'''
    Parameter: a (int): first integer number
    Parameter: b (int): second integer number
    Parameter: c (int): third integer number
    Return value: area of square with sides a, b and c
'''

area(3, 2) #returns 3
perimeter(3, 3, 3) #returns 9
```
## History of commits
* [8ba9aeb](https://github.com/voldemar64/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460) Circle and square added
* [d078c8d](https://github.com/voldemar64/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2) Docs added
* [7bc6222](https://github.com/voldemar64/geometric_lib/commit/7bc62222fec83860754efc9afb390200d4f8e00c) added: rectangle.py
* [ae706ee](https://github.com/voldemar64/geometric_lib/commit/ae706ee3040b397ef8a544c3dff1bc53f5a37a58) added triangle.py fixed: rectangle.py perimeter function
* [eede233](https://github.com/voldemar64/geometric_lib/commit/eede2333743d0c334780b1dcfe757ee96de08312) added: comments on functions
