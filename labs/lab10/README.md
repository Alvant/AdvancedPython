# Lab 10. Multiverse (Threading & Multiprocessing)

Достаточно решить первую и вторую задачу.
При решении *надо использовать процессы или потоки* (то, что даст выигрыш).


## Задача 1 («‎Множители»‎)

Надо разложить на простые множители ряд натуральных чисел, которые передаются программе как агрументы командной строки.
Результат разложения на множители каждого числа надо вывести на стандартный вывод, причём в том же порядке, как числа поступали на вход.
Например если программа называется `prime_factorization.py`, то работать она должна как-то так
```python
$ python prime_factorization.py 4 625 7 12 22
4: 2 2
625: 5 5 5 5
7: 7
12: 2 2 3
22: 2 11 
```

## Задача 2 («‎grep»‎)

Создайте папку с текстовыми файлами.
Например, можно накачать книг со сказками:
* https://archive.org/details/favouritefairyta00corniala
* https://archive.org/details/englishfairytal00jacogoog
* https://archive.org/details/grimmscompletefa00grim
* https://archive.org/details/fairytales00hauf

Надо написать программу, которая бы искала подстроку во всех файлах в заданной директории.
Подстрока и путь до директории передаются программе как аргументы командной строки.
Результат поиска — строки в файлах, где встречается указанная подстрока.
Если программа называется `custom_grep.py`, а книги лежат в папке `books` (и там, например, есть книги `Favourite-Fairy-Tales.txt` и `English-Fairy-Tales.txt`), то должна быть возможность сделать и получить что-то такое
```python
$ python custom_grep.py princess ./books
Favourite-Fairy-Tales.txt: beautiful young lady, evidently some princess,
Favourite-Fairy-Tales.txt: and handsome princess ever beheld was there,
...
English-Fairy-Tales.txt: " Sink on," cried the cruel princess, " no hand or glove
English-Fairy-Tales.txt: mill-wheels. And then they took out the princess and 
```
То есть выводится название файла и строка в нём.
Сначала должны идти строки в одном файле, потом в другом, и т.д.
Для каждого текстового файла выводимые строки должны быть упорядочены по номеру строки внутри этого файла.


## Задача 3* («‎Дубликаты»‎)

Найти все файлы-дубликаты под заданным путём.
То есть на вход программе подаётся путь до директории.
И далее надо рекурсивно обойти эту директорию и найти дубликаты.
Дубликаты — те файлы, у которых совпадают название и содержание.


## Задача 5* («‎π»‎)

Напишите программу для вычисления числа π.
Метод вычисления должен быть основан на приближении числа π частичной суммой сходящегося ряда.
Получается ли посчитать число π с точностью 100 знаков после запятой? за какое время?
