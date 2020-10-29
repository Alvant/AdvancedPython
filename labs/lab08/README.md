# Lab 8. For `i` in Iterable: Iterate

В качестве задания достаточно решить первую или вторую задачи.

## Задача 1 («‎os.walk»‎)

Надо реализовать а-ля `os.walk` с помощью итераторов.
То есть надо либо создать классы типа Iterable и Iterator (или один класс как два в одном), либо генератор, чтобы можно было с ним работать так же, как с `os.walk`.
Как параметр можно использовать только путь до корневой директории.
Например, если делать через генератор, то работа с ним должна выглядеть примерно так
```python
from typing import Iterator, List, Tuple


def custom_walk(top: str) -> Iterator[Tuple[str, List[str], List[str]]]:
    pass  # TODO: code here


for root, folders, files in custom_walk('/data/workspace'):
    # Doing something, for example:
    print(f'Folder "{root}" contains {len(folders)} folders and {len(files)} files.')
```

## Задача 2 («‎Console-Reader»‎)

Со стандартного ввода (из консоли) могу поступать числа.
Надо реализовать итератор, который бы считывал эти числа из консоли.
То есть надо либо создать классы типа Iterable и Iterator (или один класс как два в одном), либо генератор.
Например, если делать через класс итератора, то его использование должно выглядеть как-то так
```python
class ConsoleIterator:
    pass  # TODO: code here


total_sum = 0

for number in ConsoleIterator():
    total_sum = total_sum + number

print(f'Sum of entered numbers is {total_sum}')
```

## Задача 3 («‎Generator Pipeline»‎)

Есть массив чисел (возможно, очень большой массив).
Надо сделать с числами ряд преобразований.
А именно:

* убрать отрицательные числа
* возвести в квадрат оставшиеся числа
* и посчитать остатки от деления на 3 у получившихся значений

Надо реализовать эту цепочку преобразований с помощью выражений-генераторов.
Например
```python
numbers = [1, -2, 4, 3]

# TODO: code here
# result_numbers = ...
# result_numbers = ...

print(result_numbers)  # 1 1 0
```

# Ссылки

* [Презентация](http://www.dabeaz.com/generators-uk/GeneratorsUK.pdf) про пайплайны из геренаторов.