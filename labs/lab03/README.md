# Lab 3. Files & Exceptions

[Демо ноутбук по файлам](./demo/Files.ipynb).


## Задача 1 («Файловая солянка»)

Напишите программу на Питоне, которая производит следующую работу с файлами и папками.

1. Создаёт папку `hw3` в домашней директории пользователя.
(Если такая папка уже существует, то ошибки возникать не должно.)
2. В папке `hw3` создаёт текстовый файл и что-нибудь в него записывает.
Например, файл с именем `file.txt` следующего содержания:
```
Do you believe in Heaven above?
Do you believe in love?
Don't tell a lie, don't be false or untrue
It all comes back to you
```
3. Далее, создаёт некоторый JSON файл в той же папке `hw3`.
Например, [файл `file.json` следующего содержания](./demo/movies.json):
```
{
    "movies": [
        {
            "name": "Полночь в Париже",
            "release_year": 2011,
            "director": "Вуди Аллен"
        },
        {
            "name": "Гравити Фолз",
            "release_year": 2012,
            "creator": "Алекс Хирш"
        },
        {
            "name": "Окно во двор",
            "release_year": 1954,
            "director": "Альфред Хичкок"
        }
    ]
}
```
4. Далее, создаёт некоторый JSON файл в той же папке `hw3`.
Например, [такой файл `file.csv`](https://en.wikipedia.org/wiki/Oncogenomics#Copy\_number\_mutations):
```
Cancer Type,D-Loop,mRNAs,tRNAs,rRNAs,Nucleotide Position of Deletions,Increase of mtDNA copy #,Decrease of mtDNA copy #
Bladder,1,1,0,1,15642-15662,0,0
Breast,1,1,1,1,8470-13447 and 8482-13459,0,1
Oral,1,1,0,0,8470-13447 and 8482-13459,0,0
```
5. Далее, создаёт в папке `hw3` ещё какую-нибудь папку.
Например, с именем `folder`.
6. Выводит на экран отсортированный по дате создания список файлов в папке `hw3`.
Ожидаемый вывод на данном шаге:
```
file.txt file.json file.csv
```
7. Удаляет папку `hw3` (осторожно! стоит проверить путь перед тем, как удалять 😅)

При создании .json и .csv файлов надо пользоваться специальными Python библиотеками (например, `json` и `csv`)!


## Задача 2 («Custom grep»)
Напишите функцию – аналог [Питоновской `os.walk`](https://docs.python.org/3/library/os.html#os.walk):

## Задача 2* («Custom walk»)

Напишите функцию – аналог [Питоновской `os.walk`](https://docs.python.org/3/library/os.html#os.walk):
```python
def walk(top: str):

```


## Задача 3* («Custom rmtree»)

Напишите функцию – аналог [Питоновской `shutil.rmtree`](https://docs.python.org/3/library/shutil.html#shutil.rmtree):
```python
def rmtree(path: str)
```


## Задача 2* («Pluz»)

Надо написать функцию `pluz` от двух аргументов, которая работает как обычное сложение в Питоне.
С тем исключением, что если ей на вход подать число `n` и строку `s`, которая может быть успешно приведена к числовому типу,
то в результате функция `pluz` должна выдать не ошибку `TypeError`, а результат операции `n + int(s)`.

Например:
```bash
>>> def pluz(arg1, arg2):
...     # Implementation of pluz here
>>>
>>> pluz(1, 2)
3
>>> pluz('1', 2)
3
>>> pluz(1, '2')
3
>>> pluz('1', '2')
'12'
>>> pluz([1], [2])
[1, 2]
>>> pluz(1, 'a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> pluz(1, [2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'list'
```

## P.S.

* Vitamins (full version): https://en.wikipedia.org/wiki/Vitamin#List
* JavaScript's "pluz": https://github.com/denysdovhan/wtfjs#funny-math
