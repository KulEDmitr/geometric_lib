# **Описание решения Лабы №1 по ИСРПО :shipit:** 
### **Необходимые функции**
```
git clone - клонировать репозиторий в новый каталог
git branch - список, создание или удаление ветвей
git checkout - переключить ветки или восстановить файлы рабочего дерева
git add - добавляет файл в репозиторий
git commit - записать изменения в репозиторий
git log - показать журналы коммитов
git show - показать коммиты по хэшу
git merge - слияние веток
git push - отправить данные на удаленный репозиторий
```
### **Шаги работы**
- Клонируем репозиторий с помощью `git clone`
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/f4dc1718-7791-498d-bfb0-9c535a82aba3)
- Переходим в папку,создаем веточку и переходим на неё с помощью `git branch` и `git checkout`
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/0a4ccba5-1039-4cd0-a544-3fd49f244153)
- Добавляем первый файл, который был подготовлен заранее с помощью `git add`
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/73c1aada-aa88-481b-856c-7b32c22706a4)
- Коммитим с помощью `git commit`
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/d5674c2f-0a08-4eeb-9ebf-e90f171af075)
- Добавляем файл с исправленной ошибкой и коммитим 
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/1aa07404-e0cd-41fe-b587-2139f3494b02)
- Строим граф всего репозитория с помощью `git log`
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/dcc817bf-d454-4fe3-9338-ea5dbd3b5908)
- Строим граф текущей ветки 
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/b24cbbcd-a4ee-4d17-b7db-d89b6e1a1dbc)
- Берем хэши 2 последних изменений и смотрим их с помощью `git show`
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/b19645e2-1b12-4027-ae4f-b37c20639b26)
- Мерджим в ветку мастер с помощью `git merge`
![image](https://github.com/ssnchk/geometric_lib/assets/143999705/2356b830-13e3-4378-84fb-2f2ffa7315ba)


# **Описание функций**
- ## Circle.py
Имеет две функции **_area(R)_** и **_perimeter(R)_**
### **_area(R)_**
функция принимает на вход радиус окружности _R_ и выводит её площадь _πR<sup>2</sup>_
### **_perimeter(R)_**
функция принимает на вход радиус окружности _R_ и выводит её периметр _2πR_
### Пример
_**area(5)**_ --> _78.53981633974483_

**_perimeter(5)_** --> _31.41592653589793_

- ## Rectangle.py
Имеет две функции **_area(a,b)_** и **_perimeter(a,b)_**
### **_area(a,b)_**
функция принимает на вход стороны прямоугольника _a,b_ и выводит его площадь _ab_
### **_perimeter(a,b)_**
функция принимает на вход стороны прямоугольника _a,b_ и выводит его периметр _2(a+b)_
### Пример
_**area(5,10)**_ --> _50_

**_perimeter(5)_** --> _30_

- ## Square.py
Имеет две функции **_area(a)_** и **_perimeter(a)_**
### **_area(a)_**
функция принимает на вход сторону квадрата _a_ и выводит его площадь _a<sup>2</sup>_
### **_perimeter(a)_**
функция принимает на вход стороны прямоугольника _a_ и выводит его периметр _4a_
### Пример
_**area(5)**_ --> _25_

**_perimeter(5)_** --> _20_

- ## Triangle.py
Имеет две функции **_area(a,h)_** и **_perimeter(a,b,c)_**
### **_area(a)_**
функция принимает на вход сторону треугольника _a_ и высоту _h_ , проведенную к этой стороне и выводит его площадь _0.5*ah_
### **_perimeter(a)_**
функция принимает на вход стороны прямоугольника _a,b,c_ и выводит его периметр _a+b+c_
### Пример
_**area(5,4)**_ --> _10_

**_perimeter(5,10,15)_** --> _30_

## История Коммитов 
<sup>  (сверху вниз) </sup>
- L-03: Circle and square added
> 8ba9aeb
- L-03: Docs added
> d078c8d
- added rectangle
> 57f9e0d
- added triangle + error fixed
> 59f3b89
- rectangle.py commited
> c1cb85a
- square comited
> e3032e2
- triangle.py commited
> efc8c83
- circle.py commited
> 8b162b1
- Create docs.md
> d2913fe
- docs added to docs
> dcf0559
- Delete docs.md (i already have one)
> 2f7df17
- Update 1 docs.md
> 7f19c40
- Update 2 docs.md
> 6e65dce
- Update 3 docs.md
> 61f30c2
