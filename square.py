
def area(a):
    '''
    Take the length side and return the area
    :To calculate the area of a square, it is enough to know one side
    :print(area(4))  # Output: 16
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("The side length must be a number")
    if a <= 0:
        return 0
    return a * a


def perimeter(a):
    '''
    Take the length side and return the perimeter
    :print(perimeter(4))  # Output: 16
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("The side length must be a number")
    if a <= 0:
        return 0
    return 4 * a
