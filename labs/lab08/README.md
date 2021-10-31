# Lab 8. For i in Iterable: Iterate

В качестве задания достаточно решить одну из задач без звёздочки.

Во всех задачах, если не оговорено отдельно,
надо либо реализовать два класса типа "Итерируемого" и "Итератора" (или один класс как два в одном), либо генератор.


## Задача 1 («‎os.walk»‎)

Надо реализовать а-ля `os.walk` с помощью итератора (или генератора).
Как параметр можно использовать только путь до корневой директории.
Например, если делать через генератор, то работа с ним должна выглядеть примерно так:
```python
from typing import Iterable, List, Tuple


def custom_walk(top: str) -> Iterable[Tuple[str, List[str], List[str]]]:
    pass  # TODO: code here


for root, folders, files in custom_walk("/home/neo"):
    # Doing something, for example:
    print(f"Folder \"{root}\" contains {len(folders)} folders and {len(files)} files.")
```



## Задача 2 («‎Standard Input Iterator»‎)

Со стандартного ввода (из консоли) могут поступать числа.
Надо реализовать итератор (или генератор), который бы считывал эти числа из консоли.
Например, если делать через класс итератора, то его использование должно выглядеть как-то так:
```python
class ConsoleIterator:
    pass  # TODO: code here


total_sum = 0

for number in ConsoleIterator():
    total_sum = total_sum + number

print(f"Sum of entered numbers is {total_sum}")
```


## Задача 3 («‎Text File Lines Iterator»‎)

Есть текстовый файл.
Надо реализовать итератор (или генератор), который бы считывал строки этого файла.
Например, если делать через класс итератора, то его использование должно выглядеть как-то так:
```python
class FileIterator:
    def __init__(self, file_path: str):
        pass  # TODO: code here

    pass  # TODO: code here


first_letters = list()

for line in FileIterator("Waxwork.1988.720p.English.srt"):
    stripped_line = line.strip()
    first_letters.append(stripped_line[0])

possibly_some_encrypted_message = ''.join(first_letters)

print(f"First letters of the file's lines make up the following text: \"{possibly_some_encrypted_message}\".")
```

*Не забудьте, что файл следует закрыть, когда работа с ним завершена!*


## Задача 4 («‎Random Iterator»)

### Обычное условие

Надо реализовать бесконечный итератор (или генератор), который бы на каждой итерации выдавал случайное значение из фиксированного ряда значений.
Также итератору стоит добавить опциональный параметр, задающий максимальное число значений, которые может вернуть итератор
(то есть чтобы при задании этого параметра итератор уже был бы не бесконечный).

Например:
```python
from typing import List, Optional


class RandomChoiceIterator:
    def __init__(self, values: List[int], num_iters: Optional[int] = None):
        pass  # TODO: code here

    # TODO: code here


for value in RandomChoiceIterator([1, 2, 3], num_iters=5):
    print(value)
``` 

### Художественное условие

<div>
<em>
  <p align="right">
    ...Правило, которое Алиса никогда не забывала — что если выпить слишком много из пузырька с надписью «Яд», то почти наверняка, рано или поздно, почувствуешь недомогание.
  </p>
  <p align="right">
    («Алиса в Стране Чудес», Льюис Кэрролл. Перевод: Юрий Нестеренко)
  </p>
</em>
</div>

Алиса путешествует по Стране Чудес.
И на пути ей попадаются разные съедобные предметы, которые она просто не может не попробовать.
Так, время от времени ей встречаются:
пузырьки с надписью "Выпей меня", пирожные с надписью "Съешь меня", кусочки "одной" стороны гриба, и кусочки "другой" сторона гриба.
В Стране Чудес каждая из таких вкусняшек по-разному изменяет рост Алисы:
* содержимое пузырька уменьшает рост Алисы в 5 раз
* пирожное увеличивает рост Алисы в 2.5 раза
* кусочек "одной" стороны гриба уменьшает рост Алисы в 2.5 раза
* кусочек "другой" стороны гриба увеличивает рост Алисы в 5 раз

Пусть между каждой "находкой" Алисы проходит какое-то небольшое время, например 1 секунда.
Изначальный рост Алисы точно не известен, но можно считать его примерно равным 120 сантиметрам.
Путешествие Алисы начинается с того, что она выпивает один из пузырьков.
Закончиться же путешествие может только тогда, когда Алиса вновь вернётся к своему нормальному росту...

Чтобы смоделировать описанное путешествие Алисы (и понять, вернётся ли она вообще когда-нибудь из Страны Чудес),
надо реализовать бесконечный итератор, возвращающий случайное значение из фиксированного набора значений.
Если итератор реализован как класс с именем `RandomChoiceIterator` (см. пример из подсекции выше, с "обычным условием"),
то "путешествие" может быть описано так:
```python
ORIGINAL_HEIGHT = 120
DELICACIES = ["bottle", "cake", "one side of the mushroom", "other side of the mushroom"]


class RandomChoiceIterator:
    pass  # TODO: code here


current_height = ORIGINAL_HEIGHT / 5

for find in RandomChoiceIterator(DELICACIES):
    if find == "bottle":
        current_height = current_height / 5
    elif find == "cake":
        current_height = current_height * 2.5
    elif find.startswith("one side"):
        current_height = current_height / 2.5
    else:
        assert find.startswith("other side")

        current_height = current_height * 5

    if current_height == ORIGINAL_HEIGHT:
        print("Alice's Adventure is over! ...Next one is on its way?")

        break
    else:
        print(
            f"Alice found "{find}" and her current height is {current_height} != {ORIGINAL_HEIGHT}."
            f" So Alice continues her adventures in Wonderland..."
        )
```

<p align="center">
  <a href="https://en.wikipedia.org/wiki/Alice_(Alice%27s_Adventures_in_Wonderland)"><img src="./docs/images/Alice.png" width="50%" /></a>
</p>
<p align="center">
  <em>Алиса собирается выпить "пузырёк" на одной из иллюстраций Джона&nbsp;Тенниела для&nbsp;«‎Приключений&nbsp;Алисы&nbsp;в&nbsp;Стране&nbsp;чудес».</em>
</p>


## Задача 5 («‎Shuffle Me a Million Times, Million Times»‎)

Надо реализовать бесконечный итератор (или генератор), который бы на каждой итерации выдавал случайную перестановку фиксированного ряда значений.
Также итератору стоит добавить опциональный параметр, задающий максимальное число перестановок, которые может вернуть итератор
(то есть чтобы при задании этого параметра итератор уже был бы не бесконечный).

Например:
```python
from typing import List, Optional


class ShuffleIterator:
    def __init__(self, values: List[int], num_shuffles: Optional[int] = None):
        pass  # TODO: code here

    # TODO: code here


for permutation in ShuffleIterator([1, 2, 3], num_shuffles=5):
    print(permutation)
``` 



## Задача 6 («‎Cyclic Iterator»‎)

Надо реализовать бесконечный итератор (или генератор), который бы на каждой итерации выдавал следующее значение из фиксированного ряда значений.
При этом когда итератор доходит до конца ряда, он вновь возвращается в начало.
Таким образом, итератор как бы перебирает значения "по кругу".

Также итератору стоит добавить опциональный параметр, задающий максимальное число просмотра ряда значений итератором от начала до конца
(то есть чтобы при задании этого параметра итератор проходил бы конечное число "кругов").

Например:
```python
from typing import List, Optional


class CyclicIterator:
    def __init__(self, values: List[int], num_cycles: Optional[int] = None):
        pass  # TODO: code here

    # TODO: code here


for value in CyclicIterator([1, 2, 3], num_cycles=5):
    print(value)
``` 


## Задача 7* («‎Generator Pipeline»‎)

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


## Задача 8* (My Weather Forecaster)

Надо реализовать *генератор*, который бы раз в полчаса выводил на экран прогноз погоды в Долгопрудном на ближайший час.
Если нет доспута к интернету, чтоб узнать прогноз, то генератор должен выводить `"Forecast Unavailable"`.
И до тех пор, пока не получится вывести нормальный прогноз, каждая следующая попытка "предсказания" должна происходить не через полчаса, а через минуту после предыдущей.



# Ссылки

* [Презентация](http://www.dabeaz.com/generators-uk/GeneratorsUK.pdf) про пайплайны из геренаторов.
