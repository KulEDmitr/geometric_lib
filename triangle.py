def area(a, h):
'''
    Возвращает площадь треугольника по стороне и проведённой к ней высоте.
    
        Параметры:
            a (int): Сторона треугольника
            h (int): Проведённая высота
            
        Возвращаемое значение:
            triangleArea (int): Площадь треугольника стороны a и высоты h
    
'''    
return a * h / 2 

def perimeter(a, b, c):
'''
    Возвращает периметр треугольника по трём его сторонам
    
        Параметры:
            a (int): Первая сторона треугольника
            b (int): Вторая сторона треугольника
            c (int): Третья стороныа треугольника
            
        Возвращаемое значение:
            trianglePerimeter (int): Периметр треугольника со сторонами a, b, c
    
'''   
return a + b + c
