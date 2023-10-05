# Документация 
### Внутри проекта находятся модули для нахождения площади и периметра геометрических фигур(Квадрат, прямоугольник, треугольник, окружность)

## Модули

### 1. Circle.py
+ #### Функция Area получает на вход значение радиуса искомой окружности и возвращает ее площадь согласно формуле `pi*r*r`

#### Работа функции 
```python
[Python]
import circle

circle area(5) = 78,5
```

+ #### Функция Perimeter получает на вход значение радиуса искомой окружности и возвращает ее периметр согласно формуле `2*pi*r`

#### Работа функции
```python
[Python]
import circle

circle perimeter(5) = 31,4
```

### 2. Rectangle.py
+ #### Функция Area получает на вход значения 2 различных сторон искомого прямоугольника и возвращет его площадь согласно формуле`a*b`

#### Работа функции
```python
[Python]
import rectangle

rectangle area(4,8) = 32
```

+ #### Функция Perimeter получает на вход значения 2 различных сторон искомого прямоугольника и возвращает его периметр согласно формлу `(a+b)*2`

#### Работа функции 
```python
[Python]
import rectangle 

rectangle perimeter(2,7) = 18
```

### 3. Square.py
+ #### Функция Area получает на вход значение стороны искомого квадрата и возращает его площадь согласно формуле `a*a`

#### Работа функции 
```python
[Python]
import square

square area(7) = 49
```

+ #### Функция Rerimeter получает на вход значение стороны искомого квадрата и возвращает его периметр согласно формуле `a*4`

#### Работа функции 
```python
[Python]
import square

square perimeter(8) = 32
```

### 4. Triangle.py
+ #### Функция `area` получает на вход значения стороны основания и высоты к ней искомого треугольника и возвращает его площадь согласно формуле `a*h/2`

#### Работа функции 
```python
[Python]
import triangle

square area(8,6) = 24
```
+ #### Функция `perimeter` получает на вход значения всех 3 сторон искомого треугольника и возвращает его периметр согласно формуле `a+b+c`

#### Работа функции 
```python
[Python]
import triangle

square perimeter(8,6) = 24
```
## Таблица коммитов 

| Хэш коммита  | Автор коммита               | Текст коммита                    |
|--------------|-----------------------------|----------------------------------|
| 8ba9aeb      | smartiqa info@smartiqa.ru   | Circle and square added          |
| d078c8d      | smartiqa info@smartiqa.ru   | Docs added                       |
| 43a3474      | Onigiri zaharpivnev@mail.ru | create new file - rectangle.py   |
| 8f68864      | Onigiri zaharpivnev@mail.ru | create new file - triangle.py    |
| b7ea77f      | Onigiri zaharpivnev@mail.ru | fixed error in file rectangle.py |
