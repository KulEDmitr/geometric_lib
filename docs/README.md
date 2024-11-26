# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
# Documentation
This library provides functions for calculating area and perimiter of various geometric shapes. The implementation for each shape is located in a separate file.
## Rectangle
### Square
`RectangleSquare(a, b)`
Returns area of a rectangle with sides `a` and `b`
```
RectangleSquare(4, 3)
12
```
### Perimetr
`RectanglePerimetr(a, b)`
Returns perimetr of a rectangle with sides `a` and `b`
```
RectangleSquare(4, 3)
14
```
## Triangle
### Square
`TriangleSquare(a,b)`
Returns area of a triangle with base `a` and height `b`
```
TriangleSquare(4, 3)
6
```
### Perimetr
`TrianglePerimetr(a,s1,s2)`
Returns perimetr of a triangle with sides `a` and `s1` and `s2`
```
TrianglePerimetr(4,3,2)
9
```
## CommitsHistory
- `8ba9ae` [L-03: Circle and square added](https://github.com/George1487/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)
- `d078c8` [L-03: Docs added](https://github.com/George1487/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)
- `17158a` [добавил файл 1.cpp  в ветку](https://github.com/George1487/geometric_lib/commit/17158aa9edc2f8df305048bcfbf748eb08b62387)
- `7d9f95` [добавляем 2й файл по подсчету площади треугольника(с ошибкой)](https://github.com/George1487/geometric_lib/commit/7d9f95ed0b6c015badf7f26e176ec7d80de1243d)
- `c17795` [измененная прога поменял формулу  a*b  на  a*b*0,5](https://github.com/George1487/geometric_lib/commit/c17795e7f4aad4daa8c01446e857be0a8442d093)
- `64726a` [Добавили 2 файла с фигурами в котором в каждом описана работа каждой функции](https://github.com/George1487/geometric_lib/commit/64726a57a313fb275ba5584564e6bc22ce51e38c)
- `5dc3b3` [добавлена документация](https://github.com/George1487/geometric_lib/commit/5dc3b319b62614797dc162551a8beccea8107110)
## Unittest
### Цели и задачи тестирования
Основной целью тестирования является проверка работы кода, а также верности
его расчёта для вводимых значений. Также задачей является
проверка кода на вывод ошибок в случае неправильного ввода.
### Описание тестируемого продукта
Продукт содержит расчет значений площади и периметра для двух
фигур: треугольника, прямоугольника.
К требованиям тестинга относятся правильный расчет
значений, отсутствие в вводимых данных отрицательных значений и символов,
отличающихся от арабских цифр, также проверим действие программу на данных, которые больше требуемемых. 
### Область тестирования
В тестировании будут задействованы расчеты периметра и площади
вышеуказанных фигур.
### Стратегия тестирования
Тестирование будет иметь лишь функиональный тип. Определим
вручную те данные, которые введем в программу, и вычислим
то, что должно получиться по результатам программы, а далее
сравним это с выводом кода. Будем рассматривать как большие,
так и маленькие входные данные, а также допустим несколько ошибок,
чтобы посмотреть на результаты unittest.
### Критерии приемки
Верный результат работы подсчета нужных функций независимо 
от размера входных данных, не обращая внимания на время работы
### Результаты тестов

| **Функция (данные)**                                    | **Ожидаемый результат** | **Фактический результат** | **Статус теста** |
|---------------------------------------------------------|------------------------|--------------------------|------------------|
| **RectangleSquare(1000000000, 1000)**                   | 1000000000000          | -727379968               | **FAILED**       |
| **RectangleSquare(-20, 1000)**                          | 20000                  | -20000                   | **FAILED**       |
| **RectanglePerimetr(1000000000, 1000000000)**           | 2000000000             | -294967296               | **FAILED**       |
| **RectanglePerimetr(-4, 5)**                             | 18                     | 2                        | **FAILED**       |
| **TriangleSquare(1000000, 10000)**                      | 5000000000             | 705032704                | **FAILED**       |
| **TriangleSquare(-5, 10)**                              | 25                     | -25                      | **FAILED**       |
| **TrianglePerimetr(1000000000, 1000000000, 1000000000)** | 3000000000             | -1294967296              | **FAILED**       |
| **TrianglePerimetr(-5, 10, 5)**                          | 30                     | 10                       | **FAILED**       |
| **RectangleSquareTest.NormalTest**                      | 1000000                | 1000000                  | **PASSED**       |
| **RectanglePerimetrTest.NormalTest**                    | 2000                   | 2000                     | **PASSED**       |
| **TriangleSquareTest.NormalTest**                       | 50000                  | 50000                    | **PASSED**       |
| **TrianglePerimetrTest.NormalTest**                     | 1000                   | 1000                     | **PASSED**       |

