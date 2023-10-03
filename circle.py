import math


def area(r):
    ''' Return area of the circle.
    
            Accepts:
                r (int): radius of the circle

            Return:
                area (int): area of the circle
    '''
    return math.pi * r * r


def perimeter(r):
    ''' Return length of the circle

            Accepts:
                r (int): radius of the circle

            Return:
                perimiter (int): perimiter of the circle
    '''
    return 2 * math.pi * r

