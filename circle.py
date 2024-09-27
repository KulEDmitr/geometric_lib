import math


def area(r):
    ''' функция получает на вход радиус окружности и возвращает ее площадь 
    
                переменная r является радиусом окружности,
                
                например: функция получет на вход r = 5, возвращаемое значение: 78.53981633974483'''
    
	
    return math.pi * r * r


def perimeter(r):
     ''' функция получает на вход радиус окружности и возвращает ее периметр
    
                переменная r является радиусом окружности,
                
                например: функция получет на вход r = 5, возвращаемое значение: 31.41592653589793'''
    
    return 2 * math.pi * r

