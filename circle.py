import math
class Circle:
    def area(r):
        ''' 
        Вычисляет площадь оркужности радиуса r

            Входные данные:
                double r : радиус окружности

            Выходные данные:
                double area : площадь оружности
        
        Пример работы:
            >> area(5)
            >> 78,539816338
        '''
        return math.pi * r * r

    def perimeter(r):
        '''
        Вычисляет длину окружности 
        радиуса r

            Входные данные:
                double r : радиус окружности
            
            Выходные данные:
                double perimeter : длина окружности радиуса r
            
        Пример работы:
            >> perimeter(5)
            >> 31,415926535
        '''
        return 2 * math.pi * r