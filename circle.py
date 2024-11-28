import math
'''импортирует библеотеку math '''
from tests.circle_test import circ_tests

def area(r):
    '''
    принимает число r , возвращает площадь
    
    При входных: 4
    Output: 50.26548245743669
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    принимает r, возвращает периметр круга
    При входных: 4
    Output: 16
    '''
    return 2 * math.pi * r

