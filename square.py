def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Value must be number")
    if a < 0:
        raise ValueError("Value must be positive")
    return a * a


def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Value must be number")
    if a < 0:
        raise ValueError("Value must be positive")
    return 4 * a