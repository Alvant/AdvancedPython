# Lab 9. Into the Async


Помимо лабы и задания, есть [ноутбучек](./demo/Coroutines-Into-the-Async.ipynb) про асинхронность.
В качестве же задания надо решить последние два упражнения из [лабы](http://cs.mipt.ru/advanced_python/lessons/lab09.html).
Но перед задачками предлагается посмотреть следующий небольшой сюжет, иллюстрирующий идею асинхронности...


<p align="center">
  <h2>
    Моне и Асинхронность, или<br />
    или Ещё один пример, поясняющий, «про что вообще это всё»
  </h2>
</p>

Известна [серия работ](https://ru.wikipedia.org/wiki/%D0%A0%D1%83%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_(%D1%81%D0%B5%D1%80%D0%B8%D1%8F_%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD)) Клода Моне,
состоящая из нескольких десятков картин, на которых художник изобразил один и тот же Руанский собор,
с примерно одного и того же ракурса.
Но в разное время суток и в разную погоду.
Например, один из вариантов вечернего Руанского собора можно увидеть в Пушкинском музее:

<p align="center">
  <a href="https://commons.wikimedia.org/wiki/File:Claude_Monet_-_The_Rouen_Cathedral_at_Sunset_-_Pushkin_museum.jpg?uselang=ru">
    <img src="./_rouen/images/256px/Claude_Monet_-_The_Rouen_Cathedral_at_Sunset_-_Pushkin_museum.jpg" alt="The Rouen Cathedral at Sunset — Pushkin museum" />
  </a>
</p>
<p align="center">
  <em>«Руанский собор вечером» (Le Cathédrale de Rouen). Находится в Пушкинском музее (Москва).</em>
</p>

Нам же будет интересна эта серия работ Клода Моне не с художественной, а с... "времязатратной" точки зрения.
Как мог бы поступить Моне, если ему хотелось изобразить собор в разное время суток?

Первый вариант — "синхронный"[^sync].
Это как если бы Моне не приступал к новой картине, пока не закончит уже начатую.
Например, несколько дней Моне вёл бы работу над картиной, изображающей собор утром.
А днём и вечером бы ничего не делал.
Завершив "утренний собор", Моне бы приступил, например, к "собору днём".
И опять: несколько дней работа велась бы только в одно время суток, а остальное бы время Моне "бесполезно простаивал".
После "собора днём" художник бы приступил к "вечернему собору", и рисовал бы только по вечерам.

Но Моне мог бы поступить иначе, "асинхронно".
Утром Моне рисовал бы одну картину, днём&nbsp;—&nbsp;другую, а вечером&nbsp;—&nbsp;третью.
Таким образом, художник был бы занят в течение всего дня.
При асинхронном подходе несколько картин могли бы находиться в "промежуточном состоянии" в одно и то же время.
(Так Моне и работал на самом деле: "параллельно, но не одновременно" над несколькими картинами[^monet].)

Сравнение описанных подходов: синхронного и асинхронного — приведено на картинке ниже.
Очевидно, в данном случае асинхронный позволит сделать ту же работу (три картины собора) за меньшее время.

<p align="center">
  <a href="https://media.giphy.com/media/bZADBEMYl3AiNlYngs/giphy.gif">
    <img src="https://camo.githubusercontent.com/b62a3047edd43d526b75b67fcd09c13f2cbccf4a57db4260c3a3b3770d2c47ab/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f625a414442454d596c3341694e6c596e67732f67697068792e676966" alt="Rouen Cathedral: Sync Vs. Async" title="Lalala. Part 3" data-canonical-src="https://media.giphy.com/media/bZADBEMYl3AiNlYngs/giphy.gif" />
  </a>
</p>
<p align="center">
  <em>
    Руанский собор утром, днём и вечером: иллюстрация синхронной (верхняя половина картинки) и асинхронной (нижняя половина картинки) работы над картинами.
    В синхронном случае художник рисует картины последовательно, одну за другой.
	Не приступает к новой, пока не завершит начатую.
	В асинхронном&nbsp;—&nbsp;в течение одного дня художник может работать над несколькими картинами.
  </em>
</p>



## Задача 1 (оно же Упражнение 4)

От некоторого устройства в режиме реального времени приходят данные.
Необходимо написать сопрограмму, которая вычисляет среднее, дисперсию, а также количество элементов в переданном наборе данных с устройства.
Результаты работы сопрограмма должна выдавать при отправке соответствующих сигналов.


## Задача 2 (оно же Упражнение 5)

Представьте, что у вас настроено взаимодействие с сервером, от которого приходят пакеты, содержащие сообщения от различных клиентов.
Обработка каждого из клиентов должна идти в отдельном потоке.

Что нужно реализовать:

1. Корутина `connect_user` принимает данные авторизации от пользователя, открывает текстовый файл и создает на его основе корутину `write_to_file`.
2. Корутина `write_to_file(file)` записывает переданное планировщиком задач сообщение пользователя, которые записываются в файловый объект, переданный в качестве аргумента при генерации. Также принимает и обрабатывает сигнал об окончании соединения и выходит из сопрограммы.
3. Планировщик задач, распределяющий задачи по сопроцессам на каждого пользователя.

```python
import random


def user_connection(username: str):
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"


def establish_connection(auth: bool = True):
    id = f"{random.randint(0,100000000):010}"

    if auth:
        yield f"auth {id}"

    yield from user_connection(id)

    if auth:
        yield f"disconnect {id}"
```

Пример данных, приходящих от авторизованного пользователя:

```bash
>>> for i in establish_connection():
...     print(i)
auth 0081575115
0081575115 message0
0081575115 message1
0081575115 message2
0081575115 message3
0081575115 message4
0081575115 message5
0081575115 message6
disconnect 0081575115
```

Пример данных, приходящих от неавторизованного пользователя:

```bash
>>> for i in establish_connection(False):
...     print(i)
0015354373 message0
0015354373 message1
0015354373 message2
0015354373 message3
0015354373 message4
0015354373 message5
0015354373 message6
0015354373 message7
0015354373 message8
0015354373 message9
0015354373 message10
0015354373 message11
0015354373 message12
```

Данные от неавторизованных или разлогиненных пользователей обрабатываться не должны.

```python
import random


def connection():
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))

    while len(connections) > 0:
        connection = random.choice(connections)

        try:
            yield next(connection)
        except StopIteration:
            del connections[connections.index(connection)]
```

Пример сообщения, которое надо обработать, можно получить, выполнив следующий код:

```python
for i in connection():
    print(i)
```


## Ссылки

* [Статья про серию «Руанский собор»](https://marinagra.livejournal.com/151423.html)


[^sync]: Синхронный не как "синхронное плавание", а в "программистском" смысле.
Означает, что несколько действий выполняются строго одно за другим (закончил рисовать одну картину, приступил к другой).
Коротко и доступно про значения слов "синхронный" и "асинхронный" рассказано [тут](https://stackoverflow.com/questions/748175/asynchronous-vs-synchronous-execution-what-is-the-main-difference#comment57854159_748189).

[^monet]: [Выдержка](https://ru.wikipedia.org/wiki/%D0%A0%D1%83%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_(%D1%81%D0%B5%D1%80%D0%B8%D1%8F_%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD)#cite_ref-_aa50bf46a673f9c4_8-0) из Википедии (где, в свою очередь, ссылаются ещё на другой источник): "Даниэль Вильденштейн свидетельствует, что Моне работал над 9-14 полотнами одновременно."