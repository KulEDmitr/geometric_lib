

def area(a, h): 
    '''
    Take the side and the height drawn to this side and return the area using the formula
    print(area(4, 5))  # Output: 10.0
    '''
    if not isinstance(a, (int, float)) or not isinstance(h,(int, float)):
        raise TypeError("The side length must be a number")
    if a <= 0 or h <= 0: 
        return 0
    return a * h / 2

def perimeter(a, b, c): 
    '''
    Take all sides and return perimeter
    :print(perimeter(3, 4, 5))  # Output: 12
    '''
    if not isinstance(a, (int, float)) or not isinstance(b ,(int, float)) or not isinstance(c ,(int, float)):
        raise TypeError("The side length must be a number")
    if a <= 0 or b <= 0 or c <= 0 :
        return 0
    return a + b + c

# print(area.__doc__)
# print(perimeter.__doc__)