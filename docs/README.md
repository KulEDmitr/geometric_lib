# Documentation

## О проекте

> Проект представляет собой несколько модулей Python для работы с геометрическими фигурами и расчета их площадей и периметров.

## circle.py

- def area(r):

```
Возвращает площадь круга.
    Параметры:
        r (int): радиус круга

    Возвращаемое значение:
        area (int): площадь круга радиусом r
Пример вызова:
    area(1) возвращает 3,14
```

- def perimeter(r):

```
Возвращает периметр круга.
        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            perimeter (int): периметр круга радиусом r
Пример вызова:
    perimeter(1) возвращает 6,28
```

## rectangle.py

- def area(a, b):

```
Возвращает площадь прямоугольника.
    Параметры:
        a (int): сторона прямоугольника
        b (int): сторона прямоугольника

    Возвращаемое значение:
        area (int): площадь прямоугольника со сторонами a и b
Пример вызова:
    area(1, 2) возвращает 2
```

- def perimeter(a, b):

```
Возвращает периметр прямоугольника.
    Параметры:
        a (int): сторона прямоугольника
        b (int): сторона прямоугольника

    Возвращаемое значение:
        perimeter (int): периметр прямоугольника со сторонами a и b
Пример вызова:
    area(1, 2) возвращает 6
```

## square.py

- def area(a):

```
Возвращает площадь крадрата.
    Параметры:
        a (int): сторона квадрата

    Возвращаемое значение:
        area (int): площадь крадрата со стороной a
Пример вызова:
    area(2) возвращает 4
```

- def perimeter(a):

```
Возвращает периметр крадрата.
    Параметры:
        a (int): сторона квадрата

    Возвращаемое значение:
        perimeter (int): периметр крадрата со стороной a
Пример вызова:
    area(2) возвращает 8
```

## triangle.py

- def area(a, h):

```
Возвращает площадь треугольника.
    Параметры:
        a (int): сторона треугольника
        h (int): высота треугольника

    Возвращаемое значение:
        area (int): площадь треугольника со стороной a и высотой h
Пример вызова:
    area(1, 2) возвращает 1
```

- def perimeter(a, b, c):

```
Возвращает периметр треугольника.
    Параметры:
        a (int): сторона треугольника
        b (int): сторона треугольника
        c (int): сторона треугольника

    Возвращаемое значение:
        perimeter (int): периметр треугольника со сторонами a, b и с
Пример вызова:
    area(1, 2, 3) возвращает 6
```

## Тестирование

Мой проект покрыт юнит-тестами. Для их запуска выполните команду:

```sh
python3 -m unittest <имя файла>
```

Например:

```sh
python3 -m unittest circle.py 
python3 -m unittest rectangle.py 
python3 -m unittest square.py 
python3 -m unittest triangle.py
```

## History of changes

> - *[8ba9aeb3cea847b63a91ac378a2a6db758682460](https://github.com/nkich25kl/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)*:
>

- L-03: Circle and square added

> - *[d078c8d9ee6155f3cb0e577d28d337b791de28e2](https://github.com/nkich25kl/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)*:
>

- L-03: Docs added

> - *[94a2953b81eab8efa0682423910498c04498d338](https://github.com/nkich25kl/geometric_lib/commit/94a2953b81eab8efa0682423910498c04498d338)*:
>

- Add file rectangle.py

> - *[6d28d8999bf77d338b8dacf7f61743d5523ac43e](https://github.com/nkich25kl/geometric_lib/commit/6d28d8999bf77d338b8dacf7f61743d5523ac43e)*:
>

- fixed mistake in perimeter

> - *[d610c35f0820b3da00a1a6907ad8126c7dc526d8](https://github.com/nkich25kl/geometric_lib/commit/d610c35f0820b3da00a1a6907ad8126c7dc526d8)*:

- add readme.md

> - *[20af8d18d3d7fa7d913d273a2e94c2582029ad21](https://github.com/nkich25kl/geometric_lib/commit/20af8d18d3d7fa7d913d273a2e94c2582029ad21)*:

- add example in readme.md

> - *[f1cde89274b674e0dfbc6b17448d7694d5a87645](https://github.com/nkich25kl/geometric_lib/commit/f1cde89274b674e0dfbc6b17448d7694d5a87645)*:

- fix unit tests
