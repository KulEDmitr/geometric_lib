def area(a, h): 
    '''Принимает на вход сторону треугольника a и проведённую к ней высоту h, возвращает площадь треугольника
    area = triangle.area(4, 6) #Output: 12'''
    return a * h / 2 

def perimeter(a, b, c): 
    '''Принимает на вход три стороны треугольника a, b и c, возвращает периметр треугольника
    per = triangle.perimeter(4, 5, 6) #Output: 15'''
    return a + b + c