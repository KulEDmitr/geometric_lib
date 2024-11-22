int rectangle_area(int a, int b){
    /*
    Принимает числа a, b - стороны прямоугольника, возвращает площадь прямоугольника

    Пример вызова:
        area(4,5)
        Входные данные: 4 5
        Выходные данные: 20
    */
    return a * b;
}
template <typename T, typename... Args>
T rectangle_area(T first, Args... argc){
    throw 1;
}

int rectangle_perimeter(int a, int b){
    /*
    Принимает числа a, b - стороны прямоугольника, возвращает периметр прямоугольника
    
    Пример вызова:
        perimeter(4,1)
        Входные данные: 4 1
        Выходные данные: 10
    */
    return (a + b)*2;
}
template <typename T, typename... Args>
T rectangle_perimeter(T first, Args... argc){
    return first;
}