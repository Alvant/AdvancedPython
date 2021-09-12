# Lab 2. Bash


## Задача 1 («Info»)

Надо написать скрипт, который бы создавал в домашней папке пользователя, запустившего скрипт, файл `info.txt` со следующей информацией:
* время запуска скрипта
* имя пользователя
* операционную систему
* количество папок в домашней директории пользователя (без рекурсии)
* количество файлов в домашней директории пользователя (с рекурсией)

Например, пусть скрипт называется `print_info.sh`.
Пользователя пусть зовут `neo`.
А его домашняя директория `/home/neo` пусть выглядит так:
```
.
├── file1.py
├── file2.txt
└── directory1
    ├── file3.mp3
    └── directory2
        └── file5.tar
```
Тогда при запуске скрипта (например, из той же папки, где лежит скрипт)
```bash
./ print_info.sh
```
в домашней директории должен быть создан файл `info.txt` примерно следующего формата:
```
time: Вс. сент. 12 19:08:03 MSK 2021
user: neo
os: Linux
num folders in /home/neo: 1
num files in /home/neo: 4
```


## Задача 2* («Помощник»)

![](./images/rover1.jpg)

Напишите скрипт, который рекурсивно просматривает все папки в домашней директории и выводит только пути до файлов с расширением ".py".
Например, пусть структура домашней директории `/home/neo` следующая:
```
.
├── file1.py
├── file2.txt
└── directory1
    ├── file3.mp3
    └── directory2
        └── file5.py
```
Тогда скрипт должен вывести
```
/home/neo/file1.py
/home/neo/directory1/directory2/file5.py
```


## Задача 3* («Backuper»)

Напишите скрипт, который раз в два часа создаёт резервную копию домашней папки пользователя в виде `.tar` архива и сохраняет этот архив по адресу `/backup/home.tar`.

Что надо сделать, чтобы этот скрипт всегда запускался в фоне при открытии терминала?
(можно оставить комментарий в скрипте с описанием шагов)

### P.S.

В идеале такого рода скрипт (занимающийся резервным копированием) должен бы был запускаться при старте системы, а не терминала.
Чтобы работать всегда, вне завивимости от того, запущена командная оболочка или нет.
И чтобы не создавалось одинаковых процессов при открытии нескольких терминалов.


## Ссылки

![](./images/rover2.jpg)

* Консоль на Windows, в которой можно использовать команды как в Linux консоли: [Cmder](https://cmder.net/). Ещё у неё вид поприятнее, нежели чем у обычного cmd)
* Серия постов на Хабре про работу в консоли: [Bash-скрипты: начало](https://habr.com/ru/company/ruvds/blog/325522) (ссылка на первый пост).
* Тоже пост на Хабре (перевод англоязычной статьи) в целом про основные команды в терминале: [Bash для начинающих: 21 полезная команда](https://habr.com/ru/company/ruvds/blog/445270/).
* Ещё одна несложная статья с описанием того, что такое bash, с основными командами: [
The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)

---

Источник одной из картинок с собачкой: https://twitter.com/roverfromxp1