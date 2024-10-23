# geometric_lib

Библиотека geometric_lib может считать площадь и периметр таких геометрических фигур, как квадрат или круг.

Файлы:

1. circle.py :
    В ней содержится 2 функции: area и perimeter:
	    
     ***area(r)*** - принимает r - радиус окружности, возвращает math.pi * r * r - площадь окружности с радиусом r
	  пример вызова для r = 2: area(2) = math.pi * 2 * 2 = 12.566370614359172
	  
     ***perimeter(r)*** - принимает r - радиус окружности, возвращает math.pi * r * 2 - периметр окружности с радиусом r
	  пример вызова для r = 2: perimeter(2) = math.pi * 2 * 2 = 12.566370614359172

2. square.py :
    В ней содержится 2 функции: area и perimeter:
	  
     ***area(a)*** - принимает a - сторона квадрата, возвращает a * a - площадь квадрата со стороной, 
	  пример вызова для r = 2: area(2) = 2 * 2 = 4
	  
     ***perimeter(a)*** - принимает a - сторона квадрата, возвращает 4 * a - периметр квадрата со стороной a, пример вызова для r = 2: area(2) = 4 * 2 = 8

3. rectangle.py :
     В ней содержится 2 функции: area и perimeter:
      
     ***area(a,b)*** - принимает a,b - две смежных стороны прямоугольника, возвращает a * b - площадь прямоугольника со сторонами a,b; пример вызова для a = 2, b = 3: area(2) = 2 * 3 = 6
      
     ***perimeter(a,b)*** - принимает a,b - две смежных стороны прямоугольника, возвращает (a+b) * 2 - периметр прямоугольника со сторонами a,b; пример вызова для a = 2, b = 3: area(2) = (2+3) * 2 = 10

4. triangle.py :
    В ней содержится 2 функции: area и perimeter:
    
     ***area(a,h)*** - принимает a,h - сторона треугольника и высота, проведённая к ней, соответственно, возвращает a * h - площадь треугольника со сторонами a,b; пример вызова для a = 2, h = 5: area(2,5) = 2 * 5 / 2 = 5
     
     ***perimeter(a,b,c)*** - принимает a,b,c - стороны треугольника, возвращает (a+b+c - периметр прямоугольника со сторонами a,b; пример вызова для a = 2, b = 4, c = 5: area(2,4,5) = 2+4+5 = 11

История проекта: 
* [haii db2188b](https://github.com/KulEDmitr/geometric_lib/commit/db2188b0ccb9a4914cf73cbc1353510edc76eec0) добавил rectangle.py и triangle.py с комментариями

* [7b15776](https://github.com/KulEDmitr/geometric_lib/commit/7b15776363df66bad1511934e75b171e2f696e53) обновил ридми
  
* [e21d734 (HEAD -> main)](https://github.com/KulEDmitr/geometric_lib/commit/e21d734808b09b4c4bf1c2297ddcde207de753cf)  добавлена репозитория docs где хранится README.md в котором хранится информация про библиотеку geometric_lib
  
* [fd64018](https://github.com/KulEDmitr/geometric_lib/commit/fd64018f08392dece6bdeee78f4ac2acbeda3646) added comments to circle.py

* [ddd4a49](https://github.com/KulEDmitr/geometric_lib/commit/ddd4a492b6b6d01c8f571d5afd0de9cbf8b65c4c) added comments to square.py

* [d078c8d](https://github.com/KulEDmitr/geometric_lib/commit/e21d734808b09b4c4bf1c2297ddcde207de753cf) (origin/main, origin/HEAD) L-03: Docs added