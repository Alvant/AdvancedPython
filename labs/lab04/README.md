# Lab 4. Decorators & Argparse

## Задача 1 («‎Автор»‎)

Напишите декоратор `author`, который принимает на вход один строковый параметр — имя человека-автора какой-либо функции.
У функции, декорируемой `author`, должно быть появиться поле `_author`, содержащее переданное при инииализации декоратора имя автора функции.

Например
```python
>>> @author("Captain Friedrich Von Schoenvorts")
>>> def add2(num: int) -> int:
...    return num + 2
>>>
>>> print(add2._author)
Captain Friedrich Von Schoenvorts
```

## Задача 2 («‎Журнал»‎)

Напишите программу, сохраняющую некоторую информацию о человеке (такую, как имя, фамилию, возраст) в файл.
Оформите её в виде скрипта, так чтобы была возможность его запуска из командной строки.

Например, пусть скрипт называется `register.py`, а информация записывается в файл `journal.txt`.
Тогда должна быть возможность многократного запуска (в примере ниже — после запуска программы выводится содержимое файла `journal.txt`):
```bash
$ python register.py \
  --name Джим \
  --surname Хокинс \
  --age 15 \
  --sex M \
  --hobbies "treasure hunter"

$ cat journal.txt
{"name": "Джим", "surname": "Хокинс", "middle_name": null, "age": "15", "sex": "M", "married": false, "hobbies": ["treasure hunter"]}

python register.py \
  --name Джон \
  --surname Сильвер \
  --age 50 \
  --sex M \
  --married \
  --hobbies treasure alcohol

$ cat journal.txt
{"name": "Джим", "surname": "Хокинс", "middle_name": null, "age": "15", "sex": "M", "married": false, "hobbies": ["treasure hunter"]}
{"name": "Джон", "surname": "Сильвер", "middle_name": null, "age": "50", "sex": "M", "married": true, "hobbies": ["treasure", "alcohol"]}
```

### Описание параметров, которые должна быть возможность указывать в командной строке

* `--name`: имя (строка; обязательный).
* `--surname`: фамилия (строка; обязательный).
* `--middle_name`: отчество (строка; необязательный, по умолчанию `None`).
* `--age`: возраст (целое число; обязательный).
* `--sex`: пол (строка, *всего два* возможных значения: `M` и `F`; обязательный).
* `--married`: состоит ли в браке (булевское значение; необязательный). Если этот параметр *есть*, то значение `married` должно быть `True`. То есть писать надо не напрямую `<params> --married True <other params>`, а просто `<params> --married <other params>`.
* `--hobbies`: хобби (список строк; необязательный, по умолчанию `None`).

### Формат вывода

Переданная через командную строку информация должна записываться в файл.
Каждая строка — информация в формате JSON об одном человеке.
При повторных запусках программы информация дозаписывается в конец.


## Задача 3* (Accepts & Returns)

Напишите декораторы `accepts` и `returns`, которые проверяют типы параметров и возвращаемые типы декорируемой функции соответственно.
Если какой-то из типов параметров или возвращаемый тип неправильные, должна возникать ошибка `TypeError`.
Пример использования:
```python
>>> @accepts(str, int)
>>> @returns(None)
>>> def show_what_i_have(asset: str, quantity: int) -> None:
...     if quantity == 1:
...         asset = asset + 's'
...
...     print(f"I have {quantity} {asset}!")
>>>
>>> show_what_i_have("buck", 100)
I have 100 bucks!
>>> show_what_i_have(1, "pencil")
TypeError: `asset` parameter should by of type "str", not "int"!
```

## Ссылки

### Декораторы

* [Декораторы в Python: понять и полюбить](https://tproger.ru/translations/demystifying-decorators-in-python). Статья на Tproger.
* [The decorators they won't tell you about](https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb). Ноутбук с примерами и замечаниями (на английском). Это похоже на настоящий advanced level.
* [(\*) Python Wiki — PythonDecorators](https://wiki.python.org/moin/PythonDecorators). Про историю введения декораторов в Питон.
* [(\*) Python Wiki — PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary). Очень много примеров нетривиальных (и небесполезных) декораторов.
* [Awesome Python Decorator](https://github.com/lord63/awesome-python-decorator). Популярный Гитхаб репозиторий с разными ссылками по декораторам (пара ссылок выше, со звёздочками, — отсюда).

### Argparser

* [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html). Страница документации по библиотеке, с примерами (от простых к посложнее).
