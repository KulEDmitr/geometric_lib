# Документация
## Общее описание решения
geometric_lib - библиотека, с помощью которой можно узнавать периметр и площадь некоторых геометрических фигур:
- круг (окружность)
- прямоугольник
- треугольник
- квадрат

## Описание каждой функции с примерами вызова
### circle.py
area(r) - возвращает площадь круга с радиусом r  
area(1) = 3.141592653589793

perimeter(r) - возвращает периметр окружности с радиусом r  
perimiter(1) = 6.283185307179586

### rectangle.py
area(a, b) - возвращает площадь прямоугольника со сторонами a, b  
area(2, 4) = 8

perimeter(a, b) - возвращает периметр прямоугольника со сторонами a, b  
perimeter(2, 4) = 16

### triangle.py
area(a, h) - возвращает площадь треугольника со стороной a и высотой h, проведенной к этой стороне  
area(4, 5) = 10

perimeter(a, b, c) - возвращает периметр треугольника со сторонами a, b, c  
perimeter(2, 5, 4) = 11

### square.py
area(a) - возвращает площадь квадрата со стороной a  
area(5) = 25

perimeter(a) - возвращает периметр квадрата со стороной a  
perimeter(8) = 32

## История изменения проекта с хешами коммитов
commit 61e075741cfce9c391abc2b1954c7cd5aae53ff8 (HEAD -> main)
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Mon Oct 9 10:29:57 2023 +0300

    Добавил примеры вызова каждой функции

commit b42e960ad0f2a8dddc575c99b81b16b5a4933d8a (origin/main, origin/HEAD)
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Mon Oct 9 00:51:10 2023 +0300

    Добавлена документация

commit d9beddc5d4ed0deec738ec09a5b1b93968ef62d4
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Sun Oct 8 23:54:29 2023 +0300

    Добавил комментарии во все файлы репозитория

commit ac1b64f07544942f7938740f828bb9a4f6ac8f54
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Thu Sep 21 13:52:32 2023 +0300

    Mistake has been fixed
:...skipping...
commit 61e075741cfce9c391abc2b1954c7cd5aae53ff8 (HEAD -> main)
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Mon Oct 9 10:29:57 2023 +0300

    Добавил примеры вызова каждой функции

commit b42e960ad0f2a8dddc575c99b81b16b5a4933d8a (origin/main, origin/HEAD)
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Mon Oct 9 00:51:10 2023 +0300

    Добавлена документация

commit d9beddc5d4ed0deec738ec09a5b1b93968ef62d4
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Sun Oct 8 23:54:29 2023 +0300

    Добавил комментарии во все файлы репозитория

commit ac1b64f07544942f7938740f828bb9a4f6ac8f54
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Thu Sep 21 13:52:32 2023 +0300

    Mistake has been fixed

commit 17dfb68fe83fa79e1ad84ae76694d78baa044fad
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Thu Sep 21 13:51:15 2023 +0300

    New file again

commit 3a382d8eaf34c67d75f6902cb466c80fb64b143f
Author: Sergey Titarenko <serezha.titarenko.2005@gmail.com>
Date:   Thu Sep 21 13:49:27 2023 +0300

    New file has been added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
