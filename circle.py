import math

def area(r):
    """
    Returns the area of the circle.

            Parameters:
                r (int or float): radius of circle
                
            Returns:
                area (int or float): the product of pi and r^2
    """
    
    if type(r) == str:
        raise TypeError("Radius must be set as an integer!")
    if r < 0:
        raise ValueError("Radius must be greater than or equal to zero!")
        
    return math.pi * r ** 2


def perimeter(r):
    """
    Returns the perimeter of the circle.

            Parameters:
                r (int or float): radius of circle
                
            Returns:
                perimeter (int or float): the product of 2 pi and r
    """
    
    if type(r) == str:
        raise TypeError("Radius must be set as an integer!")
    if r < 0:
        raise ValueError("Radius must be greater than or equal to zero!")
        
    return 2 * math.pi * r

