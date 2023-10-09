import math


def area(r):
    '''принимает число (r) радиус круга, возвращает (pi * (r ^ 2)) площадь круга
        
        #input:  1
        #output: 3.141592653589793

        #input:  3
        #output: 28.274333882308138'''
    return math.pi * r * r


def perimeter(r):
    '''принимает число (r) снование и высоту треугольника, возвращает (2 * pi * r), периметр круга
    
        #input:  2
        #output: 12.566370614359172

        #input:  5
        #output: 31.41592653589793'''
    return 2 * math.pi * r

