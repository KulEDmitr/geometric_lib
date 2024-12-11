#include "rectangle.h"

/**
 * @brief Вычисляет площадь прямоугольника.
 *
 * Данная функция получает на вход 2 параметра: 
 * длину и ширину прямоугольника, 
 * на выходе она возвращает площадь.
 *
 * @param a Длина прямоугольника.
 * @param b Ширина прямоугольника.
 * @return Площадь прямоугольника.
 *
 * @code
 * int area = RectangleSquare(4, 3);
 * // area будет равно 12
 * @endcode
 */
int RectangleSquare(int a, int b) {
    return (a * b);
}

/**
 * @brief Вычисляет периметр прямоугольника.
 *
 * Данная функция получает на вход 2 параметра: 
 * длину и ширину прямоугольника, 
 * на выходе она возвращает периметр.
 *
 * @param a Длина прямоугольника.
 * @param b Ширина прямоугольника.
 * @return Периметр прямоугольника.
 *
 * @code
 * int perimeter = RectanglePerimetr(4, 3);
 * // perimeter будет равно 14
 * @endcode
 */
int RectanglePerimetr(int a, int b) {
    return ((a + b) * 2);
}