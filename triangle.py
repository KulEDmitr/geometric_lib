def area(a, h):
    '''
    Return area of the triangle

            Accept:
                a (int): side of the triangle
                h (int): height of the triangle
            Return:
                area (int): area of the triangle
                                
    Example:

            Accept:
                area(2, 3)

            Return:
                3
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Return perimeter of the triangle

        Accept:
            a (int): first side of the triangle
            b (int): second side of the triangle
            c (int): third side of the triangle
        Return:
            perimeter (int): perimeter of the triangle
                            
    Example:

            Accept:
                perimeter(1, 2, 3)

            Return:
                6
    '''
    return a + b + c 
