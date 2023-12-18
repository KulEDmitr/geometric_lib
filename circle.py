import math


def area(r):
    """
    Calculate the area of a circle given its radius.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The calculated area of the circle.
    
    Usage example:
    radius = 2.5
    circle_area = area(radius)
    print(f"The area of a circle with radius {radius} is: {circle_area}")
    
    Output:
    print(f"The area of a circle with radius 2.5 is: 19.634954084936208")
    """
    
    return math.pi * r * r


def perimeter(r):
    """
    Calculate the perimeter (circumference) of a circle given its radius.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The calculated perimeter of the circle.
    
    Usage example:
    radius = 3.5
    circle_perimeter = perimeter(radius)
    print(f"The perimeter of a circle with radius {radius} is: {circle_perimeter}")
    
    Output:
    print(f"The perimeter of a circle with radius 3.5 is: 21.991148575128552")
    """
    
    return 2 * math.pi * r
