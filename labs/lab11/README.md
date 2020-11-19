# Lab 11. Asyncio

В качестве задания предлагается посмотреть последние упражнения из [лабы](http://cs.mipt.ru/advanced_python/lessons/lab11.html) — которые так и озаглавлены: «Задания на дом» :)


# Задача 1 (a.k.a. «Упражнение 2», или «What is My IP?»)

Надо узнать свой IP адрес.
Есть много сервисов, которые позволяют это сделать.
Но на момент запуска программы вы не знаете, какой из сервисов доступен.
Вместо того чтобы опрашивать каждый из этих сервисов последовательно, можно запустить все запросы конкурентно и выбрать первый успешный.

```python
import asyncio
import time

from concurrent.futures import FIRST_COMPLETED
from dataclasses import dataclass  # Starting from Python 3.7

import aiohttp


@dataclass
class Service:
    name: str
    url: str
    ip_attribute: str


SERVICES = (
    Service(
        name='ipify', url='https://api.ipify.org?format=json', ip_attribute='ip'
    ),
    Service(
        name='ip-api', url='http://ip-api.com/json', ip_attribute='query'
    ),
)


async def fetch_ip(service):
    # TODO: получение IP
    raise NotImplementedError()


async def asynchronous():
    # TODO:
    #   создание футур для сервисов
    #   используйте FIRST_COMPLETED
    raise NotImplementedError()


loop = asyncio.get_event_loop()
loop.run_until_complete(asynchronous())
```


## P.S.

Потребуется `asyncio.wait()` и параметр `return_when`.
А также надо дополнительно скачать библиотеку `aiohttp`)


# Задача 2 (a.k.a. «Упражнение 3», или «My Bot Is My Best Friend»)

Надо написать Телеграм-бота, который будет на сообщение присылать соответствующее изображение.

Для выполнения задания стоит

* Установить `aiogram` — асинхронную обертку над API Телеграмма (в тексте лабы есть совет ставить версию 1.4, но не понятно, почему)
* Поговорить с `@BotFather`, создать бота и запомнить выданный токен
* Разобраться с примером эхо бота ниже
* Написать требуемый функционал (картинки можно запрашивать через поиск Яндекса или Гугла, существуют готовые API, можно написать и самостоятельно)

Ещё в лабе рекомендуют использовать WPN или прокси (если вы в РФ).
Насчёт этого тоже не понятно, обязательно это или нет (кажется, нет, но в коде оставил всё, как было).

```python
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


PROXY_URL = 'socks5://xxx.xxx.xxx.xxx'  # Вставить здесь подходящий IP

secret_token = 'XXX'  # Строка вида: 123456789:ABCDEFGHJABCDEFGHJABCDEFGHJABCDEFGHJ

bot = Bot(token=secret_token, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
```

## P.S.

Надо будет установить библиотеку `aiogram`.

## P.P.S.

Экспериментально установлено, что код с ботом может не работать в Jupyter ноутбуке — и это не из-за строчки `if __name__ == '__main__'` :)
Стоит писать всё в .py файле и его же и запускать из консоли.

## P.P.P.S

Не стоит заливать секретный токен на Гитхаб.
Стоит записать его в конфигурационном файле, считывать в процессе работы программы из конфига, и сам конфиг с токеном уже на Гитхаб отправлять *не надо*.
Конфиг может быть в любом удобном формате.
Проще всего, наверное, использовать обычный текстовый файл, а токен записывать в первой строчке.
