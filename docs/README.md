
# Библиотека Геометрических Вычислений

## Общее Описание

**Библиотека Геометрических Вычислений** предоставляет простой интерфейс для вычисления основных геометрических характеристик таких фигур, как круг, квадрат, прямоугольник и треугольник. Эта библиотека на Python предназначена для учебных целей, проектов и других задач, требующих базовых геометрических функций.

Основные возможности библиотеки включают:
- Вычисление площади и периметра квадрата.
- Вычисление площади и длины окружности круга.
- Вычисление площади и периметра прямоугольника.
- Вычисление площади и периметра треугольника.

## Описание Функций и Примеры Использования

### Модуль `circle.py`

#### `calculate_area(r)`

Вычисляет площадь круга с заданным радиусом `r`.

**Параметры:**
- `r` (float): Радиус круга.

**Возвращает:**
- `float`: Площадь круга.

**Пример использования:**

```python
from circle import calculate_area

result = calculate_area(5)
print(result)  # Вывод: 78.53981633974483
```

#### `calculate_circumference(r)`

Вычисляет длину окружности круга с заданным радиусом `r`.

**Параметры:**
- `r` (float): Радиус круга.

**Возвращает:**
- `float`: Длина окружности.

**Пример использования:**

```python
from circle import calculate_circumference

result = calculate_circumference(5)
print(result)  # Вывод: 31.41592653589793
```

### Модуль `square.py`

#### `square_area(side)`

Вычисляет площадь квадрата с заданной длиной стороны.

**Параметры:**
- `side` (float): Длина стороны квадрата.

**Возвращает:**
- `float`: Площадь квадрата.

**Пример использования:**

```python
from square import square_area

result = square_area(4)
print(result)  # Вывод: 16
```

#### `square_perimeter(side)`

Вычисляет периметр квадрата.

**Параметры:**
- `side` (float): Длина стороны квадрата.

**Возвращает:**
- `float`: Периметр квадрата.

**Пример использования:**

```python
from square import square_perimeter

result = square_perimeter(4)
print(result)  # Вывод: 16
```

### Модуль `rectangle.py`

#### `rectangle_area(length, width)`

Вычисляет площадь прямоугольника.

**Параметры:**
- `length` (float): Длина прямоугольника.
- `width` (float): Ширина прямоугольника.

**Возвращает:**
- `float`: Площадь прямоугольника.

**Пример использования:**

```python
from rectangle import rectangle_area

result = rectangle_area(5, 10)
print(result)  # Вывод: 50
```

#### `rectangle_perimeter(length, width)`

Вычисляет периметр прямоугольника.

**Параметры:**
- `length` (float): Длина прямоугольника.
- `width` (float): Ширина прямоугольника.

**Возвращает:**
- `float`: Периметр прямоугольника.

**Пример использования:**

```python
from rectangle import rectangle_perimeter

result = rectangle_perimeter(5, 10)
print(result)  # Вывод: 30
```

### Модуль `triangle.py`

#### `triangle_area(base, height)`

Вычисляет площадь треугольника по его основанию и высоте.

**Параметры:**
- `base` (float): Основание треугольника.
- `height` (float): Высота треугольника.

**Возвращает:**
- `float`: Площадь треугольника.

**Пример использования:**

```python
from triangle import triangle_area

result = triangle_area(6, 4)
print(result)  # Вывод: 12.0
```

#### `triangle_perimeter(a, b, c)`

Вычисляет периметр треугольника с заданными длинами сторон `a`, `b` и `c`.

**Параметры:**
- `a` (float): Длина первой стороны.
- `b` (float): Длина второй стороны.
- `c` (float): Длина третьей стороны.

**Возвращает:**
- `float`: Периметр треугольника.

**Пример использования:**

```python
from triangle import triangle_perimeter

result = triangle_perimeter(3, 4, 5)
print(result)  # Вывод: 12
```


# Тестирование кода: Таблица спецификаций

| Раздел                | Описание                                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------------------|
| **Цели и задачи**     | - Проверить корректность вычисления площади и периметра для различных геометрических фигур.<br>- Убедиться, что функции корректно обрабатывают некорректные входные данные.<br>- Автоматизировать тестирование ключевых операций. |
| **Описание продукта** | Модули для работы с геометрическими фигурами: прямоугольник, квадрат, треугольник и круг. <br> Реализованы функции для вычисления площади (`area`) и периметра (`perimeter`) каждой фигуры. Декоратор проверяет входные данные на корректность. |
| **Область тестирования** | - **Прямоугольник:** проверка функций `rect_compute_area` и `rect_compute_perimeter`.<br>- **Квадрат:** проверка функций `square_calculate_area` и `square_calculate_perimeter`.<br>- **Треугольник:** проверка функций `triangle_find_area` и `triangle_find_perimeter`.<br>- **Круг:** проверка функций `circle_determine_area` и `circle_determine_perimeter`. |
| **Стратегия тестирования** | Используется модуль `unittest` для организации тестов:<br>- **Функциональное тестирование:** проверка правильности математических вычислений.<br>- **Тестирование на некорректные данные:** проверка обработки ошибок, например, отрицательных чисел или неподходящих типов данных. |
| **Критерии приемки**   | - Все тесты должны успешно выполняться без ошибок.<br>- Для каждого теста на некорректные данные должно вызываться соответствующее исключение (`TypeError` или `ValueError`). |
| **Ожидаемые результаты** | - Корректные результаты вычислений для всех поддерживаемых фигур.<br>- Отчеты о выполнении тестов, включая успешные случаи и обработку ошибок. |

---

## Примеры тестов

### **Прямоугольник**
1. Площадь: 
    ```python
    self.assertEqual(rect_compute_area(15, 4), 60)  # Ожидается площадь 60
    ```
2. Периметр:
    ```python
    self.assertAlmostEqual(rect_compute_perimeter(1e8, 2e7), 2.4e8)  # Большие значения
    ```

### **Квадрат**
1. Площадь:
    ```python
    self.assertEqual(square_calculate_area(6), 36)  # Ожидается площадь 36
    ```
2. Периметр:
    ```python
    self.assertAlmostEqual(square_calculate_perimeter(5e4), 2e5)  # Погрешности учтены
    ```

### **Треугольник**
1. Площадь:
    ```python
    self.assertEqual(triangle_find_area(10, 8), 40)  # Проверка с базовыми значениями
    ```
2. Периметр:
    ```python
    self.assertAlmostEqual(triangle_find_perimeter(1e7, 1e7, 1e7), 3e7)  # Проверка равностороннего треугольника
    ```

### **Круг**
1. Площадь:
    ```python
    self.assertAlmostEqual(circle_determine_area(9), 254.46900494077323, places=5)  # Проверка с округлением
    ```
2. Периметр:
    ```python
    self.assertAlmostEqual(circle_determine_perimeter(9), 56.548667764616276, places=5)  # Проверка формулы
    ```


---

## Результаты выполнения тестов

```plaintext
................
----------------------------------------------------------------------
Ran 16 tests in 0.000s

OK

```

## История Версий
- [`fb082b59`](https://github.com/BeganovR/geometric_lib/commit/98381a23cac5a7b193e90cd135d8cbd3525f807f): Add new description and add README.md
- [`4ac89ba4`](https://github.com/BeganovR/geometric_lib/commit/e968d33def4e581d43a6d0123bd28375d304c9d8): Fix a rectangle file
- [`26d75c6d`](https://github.com/BeganovR/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460): Add new file rectangle.py
- [`26d75c6d`](https://github.com/BeganovR/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460): Circle and square added

- [`6e0a2a4f`](https://github.com/BeganovR/geometric_lib/commit/6e0a2a4fdde486236fa7694e5acb5e9c2b218fc5): Add unittests


