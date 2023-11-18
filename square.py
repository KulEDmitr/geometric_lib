def area(a):
    """
    Returns the area of the square.

            Parameters:
                a (int or float): side of square
                
            Returns:
                area (int or float): a^2
    """
    
    if type(a) == str:
        raise TypeError("Side must be set as an integer!")
    if a < 0:
        raise ValueError("Side must be greater than or equal to zero!")
 
    return a ** 2

def perimeter(a):
    """
    Returns the perimeter of the square.

            Parameters:
                a (int or float): side of square
                
            Returns:
                area (int or float): 4 a
    """
    
    if type(a) == str:
        raise TypeError("Side must be set as an integer!")
    if a < 0:
        raise ValueError("Side must be greater than or equal to zero!")
 
    return 4 * a
