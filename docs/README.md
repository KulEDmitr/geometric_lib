# **Figures**
Функции данной программы помогут найти площадь и периметр таких фигур, как *квадрат*, *прямоугольник*
*круг* и *треугольник*.
Каждая функция принимает данные о фигуре и по этим данным высчитывает периметр или площадь фигуры.
Для вычислений в функциях были использованы следующие формулы:

## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a*h/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c



## Описаниее функций
### [circle.py](https://github.com/salt-caramel/geometric_lib/edit/labwork_2/circle.py):
- *area* получает на вход радиус окружности, возвращает площадь окружности с принимаем адресом
   - Пример:\
    input: 10    output: 314
- *preimetr* получает на вход радиус окружности и возвращает длину окружности
  - Пример:\
    input: 100      output: 628

### [rectangle.py](https://github.com/salt-caramel/geometric_lib/edit/labwork_2/rectangle.py):
- *area* получает на вход длину и ширину прямоугольника, возвращает площадь площадь прямоугольника 
  - Пример:\
    input: 5, 2        output: 10
- *preimetr* получает на вход длину и ширину прямоугольника, возвращает периметр прямоугольника
   - Пример:\
     input: 5, 2        output: 14

### [square.py](https://github.com/salt-caramel/geometric_lib/edit/labwork_2/square.py):
- *area* получает на вход сторону квадрата, возвращает площадь квадрата
   - Пример:\
     input: 3    output: 9
- *preimetr* получает на вход сторону квадрата и возвращает периметр квадрата
   - Пример:\
     input: 3    output: 12

### [triangle.py](https://github.com/salt-caramel/geometric_lib/edit/labwork_2/triangle.py):
- *area* получает на вход основание и высоту треугольника, возвращает площадь треугольника
   - Пример:\
     input: 3, 6        output: 9
- *preimetr* получает на вход значение трёх сторон треугольника, возвращает периметр треугольника
   - Пример:\
     input: 2, 7, 3        output: 12


# История изменениий

1. Клонирование репозитория, который включал в себя файлы *square.py* и *circle.py*
2. Создание и добавление файла *rectangle.py* с функциями **area** и **perimetr** (1c7a987)
3. Создание и добавление файла *triangle.py* с функциями **area** и **perimetr** (47a9cd2)
4. Изменение ошибки в функции **perimetr** в *rectangle.py* и добавление файла с изменениями(efad489)
5. Дополнение функций комментариями (1fdcb86)



