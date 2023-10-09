def area(a):
    """
    Calculate the area of a square given its side.
    
    Parameters:
    a (float): The length of a side of the square.
    
    Returns:
    float: The calculated area of the square.
    
    Usage example
    side_a = 2.5
    square_area = area(side_a)
    print(f"The area of a square with side {side_a} is: {square_area}")
    
    Output:
    print(f"The area of a square with side 2.5 is: 6.25")
    """
    return a * a


def perimeter(a): 
    """
    Calculate the perimeter of a square given its side.
    
    Parameters:
    a (float): The length of a side of the square.
    
    Returns:
    float: The calculated perimeter of the square.
    
    Usage example
    side_a = 2.5
    square_perimeter = perimeter(side_a)
    print(f"The perimeter of a square with side {side_a} is: {square_perimeter}")
    
    Output:
    print(f"The perimeter of a square with side 2.5 is: 10.0")
    """
    return 4 * a
