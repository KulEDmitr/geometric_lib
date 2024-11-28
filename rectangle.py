from tests.rectangle_test import rect_tests

def area(a,b):
    '''
    принимает два числа и перемножает их
    При входных: 4 и 2
    Output: 8
    '''
    return a*b

def perimeter(a, b): 
    '''
    метод принимает два числа: а (длину) и b (ширину). Находит их удвоенную сумму (периметр прямоугольника).
    пример работы:
     perimeter(5, 3)
     16
    '''

    return (a + b) * 2

