# Lab 3. Files & Exceptions

## Задача 1 («V for Vitamin»)

Есть небольшая база данных о витаминах в виде папки [*vitamins*](./vitamins) с текстовыми файлами внутри.
Нужно написать программу, которая переводит указанную базу данных в форматы JSON и CSV.
То есть в результате должно быть получено два файла, например `vitamins.json` и `vitamins.csv`, где представлена вся та же информация о витаминах, что есть в папке *vitamins*.

При создании .json и .csv файлов надо пользоваться специальными Python библиотеками (например, `json` и `csv`)!


### Подробнее про исходные данные

Для каждого витамина в папке есть отдельный отдельный текстовый файл.
В этом файле *построчно* перечислена следующая информация:
* буквенное обозначение витамина
* химическое название
* растворимость (водо- или жирорастворимый)
* суточная потребность (в миллиграммах)
* последствия авитаминоза

Например, файл [C.txt](./vitamins/C.txt) для витамина C:
```
C
Ascorbic acid
Water
90
Scurvy
```

### Подробнее про формат результата

Пример JSON файла, где представлены два витамина из коллекции *vitamins*:
```json
[
    {
	    "vitamin": "C",
		"vitamers" "Ascorbic acid",
		"solubility": "Water",
		"daily_requirement": 90,
		"deficiency_diseases": "Scurvy"
	},
	{
	    "vitamin": "D",
		"vitamers" "Cholecalciferol, Ergocalciferol",
		"solubility": "Fat",
		"daily_requirement": 0.015,
		"deficiency_diseases": "Rickets, Osteomalacia"
	}
]
```

Пример таблицы (которую можно описать в CSV файле) где представлены два витамина из коллекции *vitamins*:
| vitamin | vitamers                        | solubility | daily_requirement | deficiency_diseases   |
| ------- | ------------------------------- |----------- | ----------------- | --------------------- |
| C       | Ascorbic acid                   | Water      | 90                | Scurvy                |
| D       | Cholecalciferol, Ergocalciferol | Fat        | 0.015             | Rickets, Osteomalacia |


## Задача 2* («Kinda JavaScript-Like +»)

Надо написать функцию `sum_js` от двух аргументов, которая работает, как обычное сложение в Питоне.
С тем исключением, что если ей на вход подать число `n` и строку `s`, которая может быть успешно приведена к числовому типу,
то в результате функция `sum_js` должна выдать не ошибку `TypeError`, а результат операции `n + int(s)`.

Например:
```bash
>>> def sum_js(arg1, arg2):
...     # Implementation of sum_js here
>>>
>>> sum_js(1, 2)
3
>>> sum_js('1', 2)
3
>>> sum_js(1, '2')
3
>>> sum_js('1', '2')
'12'
>>> sum_js([1], [2])
[1, 2]
>>> sum_js(1, 'a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum_js(1, [2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'list'
```
