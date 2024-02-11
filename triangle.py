def area(a, h):
    '''
    counts the area of triangle, using one side and height to this side
    Parameters:
        a -- length of the side (float or int)
        h -- length of the height (float or int)
    Return values:
        returns float -- area S of the triangle
    Example:
        print(area(5, 2)) // prints S (=5) of triangle with side length 5 and height 2
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    counts the perimeter of triangle, using three sides
    Parameters:
        a -- length of the first side (float or int)
        b -- length of the second side (float or int)
        c -- length of the third side (float or int)
    Return values:
        returns float or int -- perimeter
    Example:
        print(perimeter(2, 3, 5)) // prints P (=10) of triangle
    '''
    return a + b + c