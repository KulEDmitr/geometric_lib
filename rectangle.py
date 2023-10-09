def area(a, b):
    """
    Calculate the area of a rectangle given its sides.
    
    Parameters:
    a (float): The length of one side of the rectangle.
    b (float): The length of the other side of the rectangle.
    
    Returns:
    float: The calculated area of the rectangle.
    
    Usage example
    side_a = 4.5
    side_b = 2.7
    rectangle_area = area(side_a, side_b)
    print(f"The area of a rectangle with sides {side_a} and {side_b} is: {rectangle_area}")
    
    Output:
    print(f"The area of a rectangle with sides 4.5 and 2.7 is: 12.15
")
    """
    return a * b


def perimeter(a, b): 
    """
    Calculate the perimeter of a rectangle given its sides.
    
    Parameters:
    a (float): The length of one side of the rectangle.
    b (float): The length of the other side of the rectangle.
    
    Returns:
    float: The calculated perimeter of the rectangle.
    
    Usage example
    side_a = 4.5
    side_b = 2.7
    rectangle_perimeter = perimeter(side_a, side_b)
    print(f"The perimeter of a rectangle with sides {side_a} and {side_b} is: {rectangle_perimeter}")
    
    Output:
    print(f"The perimeter of a rectangle with sides 4.5 and 2.7 is: 7.2")
    """
    return 2 * (a + b)
