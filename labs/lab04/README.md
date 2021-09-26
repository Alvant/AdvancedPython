# Lab 4. Argparse & Decorators

## Задача 1 («‎Florist's»‎)

Напишите программу, сохраняющую некоторую информацию о цветке в файл.
Оформите её так, чтобы была возможность запуска из командной строки с передачей аргументов.

Например, пусть скрипт называется `add_flower.py`, а информация записывается в файл `journal.txt`.
Тогда должна быть возможность многократного запуска (в примере ниже — после запуска программы выводится содержимое файла `journal.txt`):
```bash
$ python add_flower.py \
  --name Rose \
  --country Holland \
  --petal-colour R \
  --stem-length 70 \
  --with-thorns \
  --companion-plants Solomio Snapdragon Calla_Lily

$ cat journal.txt
{"name": "Rose", "country": "Holland", "petal-colour": "R", "stem-length": 70, "with-thorns": true, "companion-plants": ["Solomio", "Snapdragon", "Calla_Lily"]}

python add_flower.py \
  --name Camomile \
  --country Russia \
  --petal-colour W \
  --stem-length 50

$ cat journal.txt
{"name": "Rose", "country": "Holland", "petal-colour": "R", "stem-length": 70, "with-thorns": true, "companion-plants": ["Solomio", "Snapdragon", "Calla_Lily"]}
{"name": "Camomile", "country": "Russia", "petal-colour": "W", "stem-length": 50, "with-thorns": false, "companion-plants": None}
```


### Описание параметров командной строки

* `--name`: название (строка; обязательный).
* `--country`: страна (строка; обязательный).
* `--petal-colour`: цвет лепестка (строка, *всего пять возможных значений*: `"R"` (красный), `"W"` (белый), `"Y"` (жёлтый), `"V"` (фиолетовый), `"B"` (синий); обязательный).
* `--stem-length`: длина стебля в сантиметрах (целое число; обязательный).
* `--with-thorns`: есть ли шипы (булевское значение; необязательный, по умолчанию `False`). Если этот параметр *есть*, то значение `with_thorns` должно становиться `True`. То есть писать надо не напрямую `<params> --with-thorns True <other params>`, а просто `<params> --with-thorns <other params>`.
* `--companion-plants`: с какими растениями хорошо сочетается в букете (список строк; необязательный, по умолчанию `None`).


### Формат вывода

Переданная через командную строку информация должна записываться в файл.
Каждая строка — информация в формате JSON об одном цветке.
При повторных запусках программы информация дозаписывается в конец файла.



## Задача 2 («‎Автор»‎)

Напишите декоратор `author`, который принимает на вход один строковый параметр — имя человека-автора какой-либо функции.
У функции, декорируемой `author`, должно появиться поле `_author`, содержащее переданное при инициализации декоратора имя автора функции.

Например
```python
>>> @author("Dany Longo")
>>> def add2(num: int) -> int:
...    return num + 2
>>>
>>> print(add2._author)
Dany Longo
```

### P.S.

Функции в Питоне — тоже объекты, которые могут иметь как методы, так и поля:
```python
>>> def func1():
>>>     pass
>>>
>>> func1.param1 = "17.5"  # just set some new parameter
>>>
>>> print(func1.param1)
17.5
>>>
>>> def func2():
>>>     func2.param1 = "Функции в Питоне — тоже объекты"
>>>
>>>     return
>>>
>>> func2()  # call once so as to initialize the parameter in the body
>>>
>>> print(func2.param1)
Функции в Питоне — тоже объекты
```


## Задача 3* («‎С днём рождения от коровки!»)

Если зайти в папку [cow](./cow) и запустить файл [cow.py](./cow/cow.py) с помощью команды
```bash
python cow.py
```
то будет создана картинка — поздравление с днём рождения от коровки:
![](./docs/happy_birthday_from_the_cow.png)

(Если не запускается — возможно, надо сначала установить библиотеку [Pillow](https://pypi.org/project/Pillow): `pip install Pillow`.)

Надо доработать файл с кодом, так чтобы его можно было запускать из командной строки *с передачей аргументов*:
имени поздравляемого, его возраста, и пути, по которому должна быть сохранена картинка-поздравление.
Например:
```bash
python cow.py --name Neo --age 5 --save-path /home/neo/hbd_neo.png
```


## Задача 5* (Timeit)

Напишите декоратор `timeit`, который измеряет время выполнения декорируемой функции.
Декоратор `timeit` должен принимать один опциональный целочисленный параметр — количество запусков функции, которые надо провести, чтобы посчитать усреднённое время выполнения (по умолчанию число запусков равно единице).

Пример использования:
```python
>>> from time import sleep
>>>
>>> @timeit
>>> def slow_add(a: int, b: int) -> int:
...     sleep(1)
...
...     return a + b
>>>
>>> slow_add(1, 2)
Execution time: 1 s
3
>>>
>>> @timeit(7)
>>> def slow_add(a: int, b: int) -> int:
...     sleep(1)
...
...     return a + b
>>>
>>> slow_add(1, 2)
Execution time: 1 s +- 0.0003 s (mean ± std. dev. of 7 runs)
3
```


## Ссылки

### Argparser

* [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html). Страница документации по библиотеке, с примерами (от простых к посложнее).


### Декораторы

* [Декораторы в Python: понять и полюбить](https://tproger.ru/translations/demystifying-decorators-in-python). Статья на Tproger.
* [The decorators they won't tell you about](https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb). Ноутбук с примерами и замечаниями (на английском). Это похоже на настоящий advanced level.
* [(\*) Python Wiki — PythonDecorators](https://wiki.python.org/moin/PythonDecorators). Про историю введения декораторов в Питон.
* [(\*) Python Wiki — PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary). Очень много примеров нетривиальных (и небезынтересных) декораторов.
* [Awesome Python Decorator](https://github.com/lord63/awesome-python-decorator). Популярный Гитхаб репозиторий с разными ссылками по декораторам (пара ссылок выше, со звёздочками, — отсюда).


### Коровка

* [Cowsay](https://en.wikipedia.org/wiki/Cowsay) — программа, благодаря которой придумано задание с коровкой.
* [Cowsay-python](https://github.com/VaasuDevanS/cowsay-python) — небольшой проект на Питоне, где есть коровка, динозавр, и ещё несколько ASCII-поздравителей.
