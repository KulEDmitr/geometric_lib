
def area(a, h): 
    '''
    Принимает числа а и h, где
        а - сторона треугольника,
	    h - высота проведенная к этой стороне.
    Возвращает площадь данного треугольника, посчитанную по формуле a * h / 2
	Examples:
    1.  input : 3 2
        output : 3
    2.  input : 4 3
        output : 6
    3.  input : 5 4
        output : 10
    4.  input : 6 5
        output : 15
    '''

    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Принимает числа a,b,c - стороны треугольника
    Возвращает периметр треугольника
	Examples:
    1.  input : 1 2 3
        output : 6
    2.  input : 2 3 4
        output : 9
    3.  input : 3 4 5
        output : 12
    4.  input : 4 5 6
        output : 15
    '''

    return a + b + c 
