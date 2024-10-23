# Общее описание решения
Этот проект содержит 4 файла с функциями для вычисления площади и периметра различных геометрических 
фигур: 
- circle.py для круга,
- rectangle.py для прямоугольника, 
- square.py для квадрата, 
- triangle.py для треугольника.

Для вычисления периметра и площади фигур используются следующие математический формулы:

## Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²

## Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2 * (a + b)
- Квадрат: P = 4a

# Описание функций с примерами вызова
`square.py`:
- `def area(a)`:
  ```python
  def area(a: float) -> float:
      """
      Возвращает площадь квадрата со стороной a

          :param a: длина стороны квадрата
          :type a: float
          :returns: площадь квадрата
          :rtype: float
        
      Пример вызова:
          s = area(5)  # В s запишется 25
      """
      return a * a
  ```
  Функция вычисляет площадь квадрата. Она принимает один аргумент: длину стороны квадрата типа float (или int) 
  и возвращает площадь квадрата типа float (или int).
  ### Пример вызова:
  ```python
  s = area(5)  # В s запишется 25
  ```

- `perimeter(a)`:
  ```python
  def perimeter(a: float) -> float:
      """
      Возвращает периметр квадрата со стороной a

          :param a: длина стороны квадрата
          :type a: float
          :returns: периметр квадрата
          :rtype: float
        
      Пример вызова:
          p = perimeter(5)  # В p запишется 20
      """
      return 4 * a
  ```
  Функция вычисляет периметр квадрата. Она принимает один аргумент: длину стороны квадрата типа float (или int) 
  и возвращает периметр квадрата типа float (или int).
  ### Пример вызова:
  ```python
  p = perimeter(5)  # В p запишется 20
  ```

`rectangle.py`:
- `def area(a, b)`:
  ```python
  def area(a: float, b: float) -> float:
      """
      Возвращает площадь прямоугольника со сторонами a, b

          :param a: длина прямоугольника
          :type a: float
          :param b: ширина прямоугольника
          :type b: float
          :returns: периметр прямоугольника
          :rtype: float
        
      Пример вызова:
          s = area(5, 2)  # В s запишется 10
      """
      return a * b 
  ```
  Функция вычисляет площадь прямоугольника. Она принимает два аргумента: длину и ширину прямоугольника типа float (или int) 
  и возвращает площадь прямоугольника типа float (или int).
  ### Пример вызова:
  ```python
  s = area(5, 2)  # В s запишется 10
  ```

- `perimeter(a, b)`:
  ```python
  def perimeter(a: float, b: float) -> float:
      """
      Возвращает периметр прямоугольника со сторонами a, b

          :param a: длина прямоугольника
          :type a: float
          :param b: ширина прямоугольника
          :type b: float
          :returns: периметр прямоугольника
          :rtype: float
        
      Пример вызова:
          p = perimeter(5, 2)  # В p запишется 14
      """
      return 2 * (a + b)
  ```
  Функция вычисляет периметр прямоугольника. Она принимает 2 аргумента: длину и ширину прямоугольника типа float (или int) 
  и возвращает периметр прямоугольника типа float (или int).
  ### Пример вызова:
  ```python
  p = perimeter(5, 2)  # В p запишется 14
  ```

`triangle.py`:
- `def area(a, h)`:
  ```python
  def area(a: float, h: float) -> float:
      """
      Возвращает площадь треугольника с основанием a и высотой h

          :param a: основание треугольника
          :type a: float
          :param h: высота треугольника
          :type h: float
          :returns: площадь треугольника
          :rtype: float
        
      Пример вызова:
          s = area(5, 2)  # В s запишется 5
      """
      return a * h / 2 
  ```
  Функция вычисляет площадь треугольника. Она принимает два аргумента: основание и высоту треугольника типа float (или int) 
  и возвращает площадь треугольника типа float (или int).
  ### Пример вызова:
  ```python
  s = area(5, 2)  # В s запишется 5
  ```

- `perimeter(a, b, c)`:
  ```python
  def perimeter(a: float, b: float, c: float) -> float:
      """
      Возвращает периметр треугольника со сторонами a, b, c

          :param a: одна сторона треугольника
          :type a: float
          :param b: вторая сторона треугольника
          :type b: float
          :param c: третья сторона треугольника
          :type c: float
          :returns: периметр треугольника
          :rtype: float
        
      Пример вызова:
          p = perimeter(5, 2, 3)  # В p запишется 10
      """
      return a + b + c
  ```
  Функция вычисляет периметр треугольника. Она принимает 3 аргумента: все стороны треугольника типа float (или int) 
  и возвращает периметр треугольника типа float (или int).
  ### Пример вызова:
  ```python
  p = perimeter(5, 2, 3)  # В p запишется 10
  ```
  
`circle.py`:
- `def area(r)`:
  ```python
  def area(r: float) -> float:
      """
      Возвращает площадь круга с радиусом r

          :param r: радиус круга
          :type r: float
          :returns: площадь круга
          :rtype: float
        
      Пример вызова:
          s = area(2)  # В s запишется 12.56
      """
      return math.pi * r * r
  ```
  Функция вычисляет площадь круга. Она принимает один аргумент: радиус круга типа float (или int) 
  и возвращает площадь круга типа float (или int).
  ### Пример вызова:
  ```python
  s = area(2)  # В s запишется 12.56
  ```

- `perimeter(r)`:
  ```python
  def perimeter(r):
      """
      Возвращает длину окружности с радиусом r

          :param r: радиус круга
          :type r: float
          :returns: длина окружности
          :rtype: float
        
      Пример вызова:
          p = perimeter(1)  # В p запишется 6.28
      """
      return 2 * math.pi * r
  ```
  Функция вычисляет длину окружности. Она принимает 1 аргумент: радиус окружности типа float (или int) 
  и возвращает длину окружности типа float (или int).
  ### Пример вызова:
  ```python
  p = perimeter(1)  # В p запишется 6.28
  ```
  
# История изменения проекта
## Коммиты

| Название                                                                                                                  | Хеш      | Автор                           | Дата             | Описание                                  |
|---------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------|------------------|-------------------------------------------|
| [project history](https://github.com/nawinds/geometric_lib/commit/2e803c3aec84e69bee0a85c664aa9c1db5579a26)               | 2e803c3a | Nikita Aksenov <me@nawinds.top> | 23/10/2024 09:46 | Добавлена история проекта                 |
| [circle docs](https://github.com/nawinds/geometric_lib/commit/c067f4fcadc268edf2e97c8c4bfc96fdf246017a)                   | c067f4fc | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:38 | Добавлена документация для круга          |
| [triangle docs](https://github.com/nawinds/geometric_lib/commit/27c6ec589b1ecf641de9e38c4bd59f781becc0a0)                 | 27c6ec58 | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:31 | Добавлена документация для треугольника   |
| [rectangle docs](https://github.com/nawinds/geometric_lib/commit/27c6ec589b1ecf641de9e38c4bd59f781becc0a0)                | d5d20b39 | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:21 | Добавлена документация для прямоугольника |
| [square docs](https://github.com/nawinds/geometric_lib/commit/b8c6acd2d2f18fef9b70974475484170cad11e95)                   | b8c6acd2 | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:12 | Добавлена документация для квадрата       |
| [General solution description](https://github.com/nawinds/geometric_lib/commit/916e5e9441fcc1492fadf9cfc1a48e3c76730789)  | 916e5e94 | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:03 | Изменен rectangle.md                      |
| [modified rectangle.py](https://github.com/nawinds/geometric_lib/commit/1d53844e0eba6a7f21ec032c65474d53a2c6b4b0)         | 1d53844e | Nikita Aksenov <me@nawinds.top> | 25/09/2024 09:02 | Изменен rectangle.md                      |
| [added triangle.py](https://github.com/nawinds/geometric_lib/commit/06fc55e6c89cb0d407407a68c6d43b530452d3a0)             | 06fc55e6 | Nikita Aksenov <me@nawinds.top> | 25/09/2024 09:01 | Добавлен triangle.md                      |
| [added rectangle.py](https://github.com/nawinds/geometric_lib/commit/74f5242e1e035e0a9263e1c6b6b7377686926b3e)            | 74f5242e | Nikita Aksenov <me@nawinds.top> | 25/09/2024 08:59 | Добавлен rectangle.md                     |
| [L-03: Docs added](https://github.com/nawinds/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)              | d078c8d9 | smartiqa <info@smartiqa.ru>     | 04/03/2021 14:55 | Добавлен README.md                        |
| [L-03: Circle and square added](https://github.com/nawinds/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460) | 8ba9aeb3 | smartiqa <info@smartiqa.ru>     | 04/03/2021 14:54 | Добавлены circle.py и square.py           |
