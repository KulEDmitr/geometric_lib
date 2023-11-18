def area(a, h):
    """
    Returns the area of the triangle.

            Parameters:
                a (int or float): side of triangle
                h (int or float): height of triangle
                
            Returns:
                area (int or float): Half of the product of a and h
    """
    
    if type(a) == str:
        raise TypeError("Side must be set as an integer!")
    if type(h) == str:
        raise TypeError("Height must be set as an integer!")
    if type(a) == str and type(h) == str:
        raise TypeError("Side and height must be set as an integer!")
    if a < 0:
        raise ValueError("Side must be greater than or equal to zero!")
    if h < 0:
        raise ValueError("Height must be greater than or equal to zero!")
    if a < 0 and h < 0:
        raise VaueError("Side and height must be greater than or equal to zero!")
 
    return a * h / 2

def perimeter(a, b, c):
    """
    Returns the perimeter of the triangle.

            Parameters:
                a (int or float): side of triangle
                b (int or float): side of triangle
                c (int or float): side of triangle
                
            Returns:
                perimeter (int or float): Sum of a, b and c
    """
    
    if (type(a) == str and (type(b) == str or type(c) == str)) or (type(b) == str and (type(a) == str or type(c) == str)) or (type(c) == str and (type(b) == str or type(a) == str)):
        raise TypeError("Sides must be set as an integer!")
    elif type(a) == str or type(b) == str or type(c) == str:
        raise TypeError("Side must be set as an integer!")
    if (a < 0 and (b < 0 or c < 0)) or (b < 0 and (a < 0 or c < 0)) or (c < 0 and (b < 0 or a < 0)):
        raise ValueError("Sides must be greater than or equal to zero!")
    elif a < 0 or b < 0 or c < 0:
        raise ValueError("Side must be greater than or equal to zero!")
        
    return a + b + c
