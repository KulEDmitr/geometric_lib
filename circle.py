import math


def area(r):
    '''
    Return area of the circle.
    
            Accept:
                r (int): radius of the circle

            Return:
                area (int): area of the circle
                
    Example:

            Accept:
                area(1)

            Return:
                3.14159265359...
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Return length of the circle

            Accept:
                r (int): radius of the circle

            Return:
                perimeter (int): perimeter of the circle
                
    Example:

            Accept:
                perimeter(1);

            Return:
                6.28318530718...
    '''
    return 2 * math.pi * r

