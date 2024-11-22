#include <cmath>

double circle_area(int r){
    /*
    Принимает число r - радиус круга, возвращает площадь круга
    
    Пример вызова:
        area(4)
        Входные данные: 4
        Выходные данные: 50.26548245743669
    */

    return M_PI * r * r;
}

template <typename T, typename... Args>
T circle_area(T first, Args... argc){
    throw 1;
}


double circle_perimeter(int r){
    /*
    Принимает число r - радиус круга, возвращает периметр круга

    Пример вызова:
        perimeter(4)
        Входные данные: 4
        Выходные данные: 25.132741228718345
    */
    return 2 * M_PI * r;
}

template <typename T, typename... Args>
T circle_perimeter(T first, Args... argc){
    throw 1;
}