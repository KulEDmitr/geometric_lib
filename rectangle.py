def area(a, b):
    """
    Calculates the area of a rectangle given its length and width.
    
    Formula:
    Area = length * width
    
    Parameters:
    a (float): The length of the rectangle.
    b (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.

    Example:
    - area(1, 1)    
    - Result: 1
    """
    return a * b

def perimeter(a, b):
    """
    Calculates the perimeter of a rectangle given its length and width.
    
    Formula:
    Perimeter = 2 * (length + width)
    
    Parameters:
    a (float): The length of the rectangle.
    b (float): The width of the rectangle.
    
    Returns:
    float: The perimeter of the rectangle.

    Exmaple:
    - perimeter(1, 1)  
    - Result: 4
    """
    return 2 * (a + b)
