double square_area(double a){
    /*
    Принимает число a - сторону квадрата, возвращает площадь квадрата
    
    Пример вызова:
        area(4)
        Входные данные: 4
        Выходные данные: 16
    */
    return a * a;
}
float square_area(float a){
    /*
    Принимает число a - сторону квадрата, возвращает площадь квадрата
    
    Пример вызова:
        area(4)
        Входные данные: 4
        Выходные данные: 16
    */
    return a * a;
}
int square_area(int a){
    /*
    Принимает число a - сторону квадрата, возвращает площадь квадрата
    
    Пример вызова:
        area(4)
        Входные данные: 4
        Выходные данные: 16
    */
    return a * a;
}
template <typename T, typename... Args>
T square_area(T first, Args... argc){
    throw 1;
}

float square_perimeter(float a){
    /*
    Принимает число a - сторону квадрата, возвращает периметр квадрата
    
    Пример вызова:
        perimeter(3)
        Входные данные: 3
        Выходные данные: 12
    */
    return 4 * a;
}
template <typename T, typename... Args>
T square_perimeter(T first, Args... argc){
    throw 1;
}