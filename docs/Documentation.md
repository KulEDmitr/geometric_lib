# Документация по проекту

## Описание проекта

В данном проекте находятся папка `.docs` с  файлом `README.md` и этой документацией, а также несколько файлов: `circle.py`, `rectangle.py`, `square.py`, `triangle.py`, каждый из них отвечает за вычисления некоторых функций для соответствующего геометрического объекта.
Ниже представлены список функций и результат их работы.

## Вычислительные функции

`circle.py` содержит в себе функции вычисления _площади круга_, которая вычисляется по формуле  $\pi r^2$, и _периметра круга_, который вычисляется по формуле $2\pi r$, где $r$ - радиус круга, заданный на входе каждой из функций, `math.pi` - значение числа $\pi$ в библиотеке `math` в Python

Пример использования:

<a href="https://ibb.co/6gvMCvL"><img src="https://i.ibb.co/dGbTYbx/image.png" alt="image" border="0" /></a>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/hcX9MjQ/image.png" alt="image" border="0" /></a>

`rectangle.py` содержит в себе функции вычисления _площади прямоугольника_ , которая вычисляется как $ab$, и _периметра прямоугольника_, который вычисляется как $2(a+b)$, где $a$ и $b$ являются сторонами прямоугольника и заданы на входе каждой из функций

Пример использования:

<a href="https://ibb.co/m55GyRM"><img src="https://i.ibb.co/N22sNFH/image.png" alt="image" border="0" /></a>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/6PYtWcG/image.png" alt="image" border="0" /></a>

`square.py` содержит в себе функции вычисления _площади квадрата_, которая вычисляется как $a^2$, и _периметра квадрата_, который вычисляется как $4a$, где $a$ - сторона квадрата,  заданная на входе каждой из функций

Пример использования:

<a href="https://ibb.co/WPvN5qV"><img src="https://i.ibb.co/dL4sM1m/image.png" alt="image" border="0" /></a>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/26X62xH/image.png" alt="image" border="0" /></a>

`triangle.py` содержите в себе функции вычисления _площади треугольника_, которая вычисляется как $ah/2$, где $a$ - сторона прямоугольника и $h$ - высота, опущенная на сторону $a$ из противоположной стороне вершины треугольника, и _периметра треугольника_, который вычисляется как $a+b+c$, где $a,b,c$ - стороны треугольника

Пример использования:

<a href="https://ibb.co/TRxNmr8"><img src="https://i.ibb.co/mtVP6Sq/image.png" alt="image" border="0" /></a>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/sWL7MDk/image.png" alt="image" border="0" /></a>

## История изменения проекта
[commit 8ba9aeb](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460) - добавление функций вычисления площади и периметра для круга и квадрата

[commit d078c8d](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2) - добавление `README.md` в папку .docs

[commit c63b0fd](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/c63b0fd9555420054a1d1c37f0bb049ea431dffb) - добавление функций вычисления периметра и площади для прямоугольника

[commit  d707ead](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/d707ead983ef48c9d443711f3ddcdb29924c127f) - добавление функций вычисления периметра и площади для треугольника

[commit 1c0dcdb](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/1c0dcdb5f7f82ce5e6bc523adfbde2d60818f6b8) - исправление функции вычисления периметра для прямоугольника

[commit aabd1f4](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/aabd1f4503d444edc52608f350feec67ca8ee154) - добавлено описание функций для круга

[commit 5b3e10d](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/5b3e10d20aea6fa9a0ec07b649b67832db37257d) - добавлено описание функций для прямоугольника

[commit f2b59f8](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/f2b59f852e385494127e64f4aaef83695a4655cc) - добавлено описание функций для квадрата

[commit 3996851](https://github.com/VyacheslavAtamanyuk/geometric_lib/commit/39968514f0345ddee5b6f960de90d8c6c9ed92f5) - добавлено описание функций для треугольника
