def area(a, h): 
    return a * h / 2 
#функция для вычисления площади треугольника
#входные значения a - сторона на которую опускают высоту h - высота
#выходные значения площадь треугольника

def perimeter(a, b, c): 
    return a + b + c 
#функция для вычисления периметра треугольника
#входные значения a - 1 сторона b - 2 сторона c - 3 сторона
#выходные значения периметр треугольника

int a = 5
int b = 2
int c = 4
int h = 3

print( area( a, h ) )
#вызов функции для вычисления площади зная сторону а = 5 и высоту h = 3
print( perimetr( a, b, c ) )
#вызов функции для вычисления периметра зная стороны a = 5 b = 2 c = 4
