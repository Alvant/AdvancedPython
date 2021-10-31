# Lab 9. Into the Async


![](https://media.giphy.com/media/bZADBEMYl3AiNlYngs/giphy.gif "Lalala. Part 3")






Помимо лабы и задания, есть [небольшой ноутбук](./demo/Coroutines-Into-the-Async.ipynb) про асинхронность.

В качестве же задания надо решить последние два упражнения из [лабы](http://cs.mipt.ru/advanced_python/lessons/lab09.html).

## Задача 1 (a.k.a. Упражнение 4)

От некоторого устройства в режиме реального времени приходят данные.
Необходимо написать сопрограмму, которая вычисляет среднее, дисперсию, а также количество элементов в переданном наборе данных с устройства.
Результаты работы сопрограмма должна выдавать при отправке соответствующих сигналов.

## Задача 2 (a.k.a. Упражнение 5)

Представьте, что у вас настроено взаимодействие с сервером, от которого приходят пакеты, содержащие сообщения от различных клиентов. Обработка каждого из клиентов должна идти в отдельном потоке.

Вещи, которые надо реализовать:

1. Корутина `connect_user` принимает данные авторизации от пользователя, открывает файл с названием .txt и создает на его основе корутину `write_to_file`.
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
