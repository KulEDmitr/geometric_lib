int triangle_area(int a, int h){ 
    /*
    Принимает число a - сторону треугольника, на котоорую опущена высота h, возвращает площадь треугольника
    
    Пример вызова:
        area(4,2)
        Входные данные: 4, 2
        Выходные данные: 4
    */
    return a * h / 2 ;
}

float triangle_area(float a, float h){ 
    throw 1;
}

template<typename T,typename... Args>
T triangle_area(T first, Args... argc){
    throw 1;
}

int triangle_perimeter(int a, int b, int c){
    /*
    Принимает числа a, b ,c - стороны треугольника, возвращает периметр треугольника
    
    Пример вызова:
        perimeter(4,5,4)
        Входные данные: 4, 5, 4
        Выходные данные: 13
    */
    return a + b + c;
}

template<typename T,typename... Args>
T triangle_perimeter(T first, Args... argc){
    throw 1;
}