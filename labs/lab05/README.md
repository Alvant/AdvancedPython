# Lab 5. OOP (ООП ("о-о-пэ"))

Достаточно решить любую задачу.
При этом надо

> (c) Руководствоваться принципами полиморфизма, наследования и инкапсуляции.


## Задача 1 («Кино»)

*Ситуация*: люди (`Human`) любят смотреть кино (`Movie`), но некоторые фильмы нежелательно смотреть по возрастному ограничению...

Фильм (`Movie`) определяется следующими признаками:
* название (строка)
* режиссёр (строка)
* год выпуска (целое число)
* страна (строка)
* продолжительность в минутах (целое число)
* возрастной рейтинг — минимальный допустимый возраст для просмотра (целое число)

У человека же (`Human`) есть следующие атрибуты:
* имя
* пол
* год рождения

Чтобы понять, можно ли данному человеку `human` смотреть фильм `movie`,
у каждого фильма должен быть метод `is_allowed(human)`,
который возвращает `True` или `False` в зависимости от того,
разрешено или нет человеку смотреть фильм:
```python
movie = Movie(
  name="Dune", director="Denis Villeneuve", year=2021,
  country="USA", duration=155, age_rating=13
)
human = Human(name="Neo", sex="M", year_of_birth=1964)

print(movie.is_allowed(human))  # True
```

Также можно выделить "особого вида фильмы": мультфильмы (`Cartoon`).
Как фильмы, у которых есть ещё один атрибут "техника создания" `technique` (рисованный, пластилиновый, ...).
Среди мульфильмов же отдельно можно выделить ещё аниме (`Anime`) — как рисованные мульфильмы, у которых страной производства всегда является Япония.

Надо реализовать описанные классы `Human`, `Movie`, `Cartoon`, и `Anime`.


## Задача 2 («Салон»)

*Ситуация*: люди (`Human`) приходят в салон красоты, где работают разные специалисты...
 
Будем считать, что человек (`Human`) обладает следующими характеристиками:
* имя (строка)
* возраст (целое число)
* пол (строка; два возможных значения: `"M"` и `"F"`)
* средняя длина волос в сантиметрах (целое число)
* средняя длина ногтей в миллиметрах (целое число)
* цвет ногтей (строка; по умолчанию — бесцветные)

Все сотрудники салона умеют выполнять свою работу `do_job(human)`.
Но работа у всех разная.
Так, в салоне работают следующие специалисты:
* Мастер маникюра: уменьшает длину ногтей на 1 (если можно уменьшить) и красит ногти в случайный цвет (красный, фиолетовый или зелёный)
* Парикмахер: уменьшает длину волос на 1 (если можно уменьшить)
* Барбер: как парикмахер, но стрижёт только мужчин. Если приходит женщина — то бросает исключение `ValueError`.

Например:
```python
neo = Human(
  name="Neo", sex="M", year_of_birth=1964,
  hair_length=10, nail_length=2
)
trinity = Human(
  name="Trinity", sex="F", year_of_birth=1967,
  hair_length=30, nail_length=5
)

manicurist = Manicurist(name="Samara", sex="F", year_of_birth=1992)
barber = Barber(name="Bob", sex="M", year_of_birth=1987)

manicurist.do_job(neo)
# Теперь у Нео ногти длины 1 и, например, фиолетовые

barber.do_job(neo)
# Теперь у Нео волосы длины 9

barber.do_job(trinity)
# А тут программа падает с исключением ValueError...
```

Надо реализовать классы `Human`, `Manicurist`, `Hairdresser`, и `Barber`.


## Задача 3 («Куриные дела»)

*Ситуация*: жили-были яйцо, цыплёнок, курица, и петух...

У цыплёнка (`Chicken`), курицы (`Hen`) и петуха (`Cock`) из признаков есть пол (у цыплёнка — либо мужской, либо женский).
А также имя (при этом имя либо задано, либо отсутствует).
У всех, включая яйцо (`Egg`), есть ещё некоторый вес в граммах.
У всех яиц одинаковый вес — 50.

Цыплёнок, курица и петух умеют есть и ходить:
* `eat(n)` — увеличивает вес на `n` грамм
* `run(n)` — уменьшает вес на `n` грамм

Например:
```python
hen = Hen(name="Julie", weight=3000)

hen.eat(60)  # Теперь вес 3060
hen.run(5)   # А теперь — 3055
```

Помимо этого петух ещё умеет кукарекать:
```python
cock = Cock(name="Bruce", weight=3800)

cock.crow()  # Выводится строка: "Сock-a-doodle-doo!"
```

Курица же может нести яйца (при этом создаётся новое яйцо):
```python
hen = Hen(name="Anna", weight=3000)

egg = hen.lay()
```

Яйцо может "вылупляться": в результате получается цыплёнок.
При этом с вероятностью 1/2 цыплёнок будет мужского пола, и с вероятностью 1/2 — женского.
"Вылупиться" яйцо может только один раз.
При повторной попытке вылупиться должно возникать исключение `Exception`:
```python
egg = Egg()

chicken = egg.hatch()  # Получается цыплёнок
chicken = egg.hatch()  # А тут падаем с исключением Exception...
```

У цыплёнка есть возможность "вырасти": если цыплёнок мужского пола, получается петух, иначе — курица.
Как и с яйцом, нельзя вырасти несколько раз (будет исключение `Exception`):
```python
chicken = Chicken(name="Yellowy", sex='F')

adult = chicken.grow()  # Получается курица
adult = chicken.grow()  # А тут падаем с исключением Exception...
```

Надо реализовать классы `Egg`, `Chicken`, `Hen`, и `Cock`.

---

[![](./images/matrix4.png)](https://youtu.be/eC4PI9y6AVQ)