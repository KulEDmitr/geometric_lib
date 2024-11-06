
def area(a, b): 
    '''
    Take the lengths of the two sides and return the area
    :print(area(4, 5))  # Output: 20'
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("The side length must be a number")
    if a <= 0 or b <=0 :
        return 0
    return a * b

def perimeter(a, b): 
    '''
    Take the lengths of the two sides and return perimeter using the formula 2a + 2b
    : print(perimeter(4, 5))  # Output: 18
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("The side length must be a number")
    if a <=0 or b <=0 :
        return 0
    return (a + b ) * 2