def area(a, h): 
    """
    Calculate the area of a triangle given its base and height.

    Parameters:
    a (float): The base length of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The calculated area of the triangle.
    
    Usage example
    base = 4.5
    height = 2.7
    triangle_area = area(base, height)
    print(f"The area of a triangle with base {base} and height {height} is: {triangle_area}")
    
    Output:
    print(f"The area of a triangle with base 4.5 and height 2.7 is: 6.075")
    """
    
    return a * h / 2 


def perimeter(a, b, c): 
    """
    Calculate the perimeter of a triangle given its three side lengths.

    Parameters:
    a (float): The length of side 'a' of the triangle.
    b (float): The length of side 'b' of the triangle.
    c (float): The length of side 'c' of the triangle.

    Returns:
    float: The calculated perimeter of the triangle.
    
    Usage example
    side_a = 4.5
    side_b = 2.7
    side_c = 3.8
    triangle_perimeter = perimeter(side_a, side_b, side_c)
    print(f"The perimeter of a triangle with sides {side_a}, {side_b}, and {side_c} is: {triangle_perimeter}")
    
    Output:
    print(f"The perimeter of a triangle with sides 4.5, 2.7, and 3.8 is: 11.0")
    """
    
    return a + b + c 
