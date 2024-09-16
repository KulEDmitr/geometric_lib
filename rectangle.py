def area(a, b):
    """
    Returns the area of the rectangle.

            Parameters:
                a (int or float): side of rectangle
                b (int or float): side of rectangle
                
            Returns:
                area (int or float): Product of a and b
    """
    
    if type(a) == str and type(b) == str:
        raise TypeError("Sides must be set as an integer!")
    elif type(a) == str or type(b) == str:
        raise TypeError("Side must be set as an integer!")
    if a < 0 and b < 0:
        raise ValueError("Sides must be greater than or equal to zero!")
    elif a < 0 or b < 0:
        raise ValueError("Side must be greater than or equal to zero!")
 
    return a * b

def perimeter(a, b):
    """
    Returns the perimeter of the rectangle.

            Parameters:
                a (int or float): side of rectangle
                b (int or float): side of rectangle
                
            Returns:
                perimeter (int or float): 2 sums of a and b
    """
    
    if type(a) == str and type(b) == str:
        raise TypeError("Sides must be set as an integer!")
    elif type(a) == str or type(b) == str:
        raise TypeError("Side must be set as an integer!")
    if a < 0 and b < 0:
        raise ValueError("Sides must be greater than or equal to zero!")
    elif a < 0 or b < 0:
        raise ValueError("Side must be greater than or equal to zero!")
 
    return 2*(a + b)
