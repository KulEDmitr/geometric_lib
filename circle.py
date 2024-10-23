import math

def area(r):
    """
    Calculates the area of a circle given its radius.
    
    Formula:
    Area = π * r^2
    
    Parameters:
    r (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.

    Example:
    - area(1)          
    - Result: 3.1416
    """
    return math.pi * r * r

def perimeter(r):
    """
    Calculates the circumference (perimeter) of a circle given its radius.
    
    Formula:
    Perimeter = 2 * π * r
    
    Parameters:
    r (float): The radius of the circle.
    
    Returns:
    float: The circumference of the circle.

     Example:
    - perimeter(1)    
    - Result: 6.2832
    """
    return 2 * math.pi * r
