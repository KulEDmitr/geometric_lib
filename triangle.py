def area(a, h):
    """
    Принимает значения стороны и высоты треугольника, возвращает площадь треугольника.

            Параметры:
                a (int): длина стороны треугольника (десятичное целое число);
                h (int): длина высоты треугольника (десятичное целое число);

            Возвращаемое значение:
                Площадь треугольника (Произведение a и h, делённое на 2).

            Пример вызова функции:

                a = 5 # Length of the first side
                h = 10 # Length of the height
                S = area(a,h)
                print("Area is equal to", S) # Output: "Area is equal to 50"
        """
    return a * h / 2 


def perimeter(a, b, c):
    """
    Принимает значения сторон треугольника, возвращает периметр треугольника.

            Параметры:
                a (int): длина первой стороны (десятичное целое число);
                b (int): длина второй стороны (десятичное целое число);
                c (int): длина третьей стороны (десятичное целое число);

            Возвращаемое значение:
                Периметр прямоугольника (сумма сторон a, b и c).

            Пример вызова функции:

                a = 5 # Length of the first side
                b = 10 # Length of the second side
                c = 15 # Length of the third side
                P = perimeter(a,b,c)
                print("Perimeter is equal to", P) # Output: "Perimeter is equal to 30"
        """
    return a + b + c
