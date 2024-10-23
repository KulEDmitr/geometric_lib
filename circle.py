import math
'''Import library with mathematical functional and constants'''

def area(r):
    '''
    Take the radius and return the area using the formula πR²
    : Example print(area(4))  # Output: 50.26548245743669
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    return the perimeter using the formula 2πR
    : Example print(perimeter(4))  # Output: 25.132741228718345
    '''
    return 2 * math.pi * r

