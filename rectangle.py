def area(a, b):
    """Принимает значения сторон прямоугольника, возвращает площадь прямоугольника.

        Параметры:
            a (int): длина первой стороны (десятичное целое число);
            b (int): длина второй стороны (десятичное целое число);

        Возвращаемое значение:
            Площадь прямоугольника (Произведение a и b).

        Пример вызова функции:

            a = 5 # Length of the first side
            b = 10 # Length of the second side
            S = area(a,b)
            print("Area is equal to", S) # Output: "Area is equal to 50".
    """
    return a * b


def perimeter(a, b):
    """Принимает значения сторон прямоугольника, возвращает периметр прямоугольника.

            Параметры:
                a (int): длина первой стороны (десятичное целое число);
                b (int): длина второй стороны (десятичное целое число);

            Возвращаемое значение:
                Периметр прямоугольника (удвоенная сумма a и b).

            Пример вызова функции:

                a = 5 # Length of the first side
                b = 10 # Length of the second side
                P = perimeter(a,b)
                print("Perimeter is equal to", P) # Output: "Area is equal to 30".
        """
    return 2*a + 2*b
