def area(a, b):
    '''
    counts the area of rectangle, using two sides
    Parameters:
        a -- length of the first side (float or int)
        b -- length of the second side (float or int)
        please note that sides should not be parallel to each other
    Return values:
        returns float -- area S of the rectangle
    Example:
        print(area(5, 2)) // prints S (=10) of rectangle with sides 5 and 2
    '''
    return a * b

def perimeter(a, b):
    '''
    counts the perimeter of rectangle, using two sides
    Parameters:
        a -- length of the first side (float or int)
        b -- length of the second side (float or int)
        please note that sides should not be parallel to each other
    Return values:
        returns float -- perimeter P of the rectangle
    Example:
        print(area(5, 2)) // prints P (=14) of rectangle with sides 5 and 2
    '''
    return (a + b) * 2