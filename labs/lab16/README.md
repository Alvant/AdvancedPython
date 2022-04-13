# Lab 16. NumPy («Нам-Пай» / «Нам-Пи»)

Все задания можно оформить в .ipynb ноутбуке: кажется, в данном случае это более подходящий вариант оформления.

Во всех заданиях (включая задания после первого, но и в первом тоже) нельзя использовать циклы: только функционал `numpy` (работа с векторами и матрицами).


## Задание 1

Последнее из [лабы](http://cs.mipt.ru/advanced_python/lessons/lab16.html).
Ниже приведена копия условия с сайта.

Рассмотрим функцию f на отрезке [1, 15]:

<!-- <img src="https://render.githubusercontent.com/render/math?math=f(x) = \sin(x / 5) * \exp(x / 10) + 5 * \exp(-x / 2)"> -->

<p align="center">
    <img src="./images/func_equation.svg" title="f(x) = \sin(x / 5) \exp(x / 10) + 5 \exp(-x / 2)" />
</p>

<p align="center">
    <img src="./images/func_plot.png" width="50%" />
</p>

Она может описывать, например, зависимость оценок, которые выставляют определенному сорту вина эксперты, в зависимости от возраста этого вина.
Мы хотим приблизить сложную зависимость с помощью функции из определенного семейства.
В этом задании мы будем приближать указанную функцию с помощью многочленов.

Как известно, многочлен степени `n` (то есть w<sub>0</sub> + w<sub>1</sub> x + w<sub>2</sub> x<sup>2</sup> + ... + w<sub>n</sub> x<sup>n</sup>) однозначно определяется любыми n + 1 различными точками, через которые он проходит.
Это значит, что его коэффициенты w<sub>0</sub>, ..., w<sub>n</sub> можно определить из следующей системы линейных уравнений:

<p align="center">
    <img src="./images/system_of_equations.png" />
</p>

где через x<sub>1</sub>, ..., x<sub>n</sub>, x<sub>n + 1</sub> обозначены точки, через которые проходит многочлен, а через f(x<sub>1</sub>), ..., f(x<sub>n</sub>), f(x<sub>n&nbsp;+&nbsp;1</sub>) — значения, которые он должен принимать в этих точках.

Воспользуемся описанным свойством, и будем находить приближение функции многочленом, решая систему линейных уравнений.

1. Сформируйте систему линейных уравнений (то есть задайте матрицу коэффициентов A и свободный вектор b) для многочлена первой степени, который должен совпадать с функцией f в точках 1 и 15. Решите данную систему с помощью функции `numpy.linalg.solve`. Нарисуйте функцию f и полученный многочлен. Хорошо ли он приближает исходную функцию?
2. Повторите те же шаги для многочлена второй степени, который совпадает с функцией f в точках 1, 8 и 15. Улучшилось ли качество аппроксимации?
3. Повторите те же шаги для многочлена третьей степени, который совпадает с функцией f в точках 1, 4, 10 и 15. Хорошо ли он аппроксимирует функцию? Коэффициенты данного многочлена (четыре числа в следующем порядке: w<sub>0</sub>, w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub>) являются ответом на задачу. Округлять коэффициенты не обязательно, но при желании можно произвести округление до второго знака (т.е. до числа вида 0.42).


## Задание 2

Есть два вектора одинаковой длины: `x` и `y`.
Надо найти количество позиций, для которых элементы в обоих векторах ненулевые.
Число позиций, для которых хотя бы в одном из двух векторов `x` и `y` есть ненулевой элемент.

Например:
```
x = [1, 0, 1, 1, 0, 1, 1]
y = [0, 2, 0, 2, 0, 2, 0]

Answer: 2, 6
```


## Задание 3

В векторе `x` надо повторить каждый элемент `N` раз подряд.

Например:
```
x = [1, 2, 0], N = 3

Answer: [1, 1, 1, 2, 2, 2, 0, 0, 0]
```


## Задание 4

В векторе `x` надо найти максимальный элемент среди тех, перед которыми стоит
ноль.

Например:
```
x = [0, 11, 0, 0, -7, 2, 0, 4, 0]

Answer: 11
```


## Задание 5

В векторе `x` надо заполнить каждый нулевой элемент предыдущим ненулевым
значением.

Например:
```
x = [8, 0, 0, 1, 0, 0, 0, -17.5, 0]

Answer: [8, 8, 8, 1, 1, 1, 1, -17.5, -17.5]
```


## Задание 6

Надо вычислить приближённое значение функции
f(x)&nbsp;=&nbsp;ln(1 + x)
в точке x<sub>0</sub> с помощью разложения в ряд Тейлора N-го порядка в окрестности нуля:

<p align="center">
    <img src="./images/log.svg" title="\ln (1 + x) \approx \sum\limits_{n=1}^N \frac{(-1)^{n+1}x^n}{n}" />
</p>


## Задание 7

Дана матрица X «объекты-признаки» размера m&nbsp;x&nbsp;n:
число строк m — это количество объектов,
а число столбцов n — количество признаков.
Каждая строка представляет собой описание объекта выборки в виде набора значений его признаков.
Каждый же столбец содержит значения определённого признака на всех объектах выборки.

Например, матрица X, соответствующая некоторой совокупности из трёх объектов с двумя признаками:
```
    ┌        ┐
    │ 175  4 │
X = │  20  2 │
    │  25  8 │
    └        ┘
```

(где первый столбец может представлять, например, "рост" в сантиметрах,
а второй столбец — количество "конечностей")

Надо найти выборочное среднее и ковариационную матрицу выборки X,
не пользуясь специальными `numpy` функциями `mean` и `cov`.


# Ссылки

* [NumPy Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html): не обязательно приводить тензоры к одинаковым размерностям при сложении и поэлементном умножении
* [NumPy Indexing](https://numpy.org/doc/stable/reference/arrays.indexing.html): не всегда подматрица — ссылка на тот же кусок исходной матрицы (также см. про `flatten`, `ravel` и `reshape`)