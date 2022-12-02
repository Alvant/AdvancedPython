# Lab 12. Re

В качестве задания предлагается решить любые две задачи из приведённых ниже.
При решении надо использовать регулярные выражения!


## Задача 1 («Money, Money, Money»)

Надо найти все денежные суммы в тексте.
Пусть валюта указывается только в рублях, долларах и евро.
Например, в тексте
```
Молоко стоит $2.
Один билет в Сан-Франциско и обратно стоит 30000 ₽, а 2 билета — всего 50000₽!
€1 = 83₽ (2021 год, 22 ноября).
```
программа должна найти числа `2`, `30000`, `50000`, `1`, `90`.


## Задача 2 («Books»)

Надо найти все названия книг в тексте.
Например, в тексте
```
Я сейчас читаю «Случайную вакансию» Джоан Роулинг.
Не знаю, как тебе, а мне книга «Террор» Симмонса показалась очень затянутой.
Конечно, я читал Гарри Поттера! Но вот фильм «Гарри Поттер и Кубок огня» мне совершенно не понравился!
```
упоминаются книги (форма слов — как в тексте): `Случайную вакансию`, `Террор`, `Гарри Поттера`.


## Задача 3 («Functions»)

Есть файл с Python кодом.
Надо найти в нём все функции (асинхронные можно пропустить).
Примем, что отступы состоят из пробелов.
Например, в файле с таким содержимым
```python
def print_hello():
    print("Hello!")

class Goodbyer:
    def print_goodbye(self):
        print('Bye!')
```
программа должна найти блоки
```python
def print_hello():
    print("Hello!")
```
и
```python
def print_goodbye(self):
    print('Bye!')
```


## Задача 4 («Black Friday»)

Надо снизить цену всех воздушных шариков, "убрав" класс единиц из стоимости.
Например, список цен
```
Шарик красный: 100
Шарик синий: 110
Кофе зерновой: 1000
Шарик пурпурный: 200
Кекс с изюмом: 200
```
надо преобразовать в
```
Шарик красный: 10
Шарик синий: 11
Кофе зерновой: 1000
Шарик пурпурный: 20
Кекс с изюмом: 200
```


## Задача 5 («Where the Boys Are»)

<div>
<em>
  <p align="right">
    In the crowd of a million people, I'll find my valentine...
  </p>
</em>
</div>

Надо найти имена всех мальчиков в списке людей.
Каждая строчка в списке — имя и фамилия.
Например, в списке
```
Тихон Корзюков
Истратов Женя
Лиза Воронцова
Брыгина Ольга
Данила Тарасов
```
должны быть найдены имена `Тихон`, `Женя`, `Данила`.


## Задача 6 («ДНК»)

В некоторых словах есть подслово "днк".
Например, в слове "без**д**ель**н**и**к**".
Надо преобразовать текст так, чтобы во всех таких словах "исчезли" все буквы, кроме подслова "днк".
Под "исчезанием" буквы имеется в виду замена её на пробел.

Например, следующий текст
```
Зазвонил будильник — и начался девичник.
Настоящий художник должен быть с чудинкой.
"Мой любимый раздел физики — конечно же, термодинамика!" — сказал всадник.
Он меня не услышал, потому что засмотрелся на родинку на щеке прекрасной индианки.
Один из двойняшек нашёл в заповеднике большой подсолнечник и — вот дьяволёнок! — срезал его.
```
преобразуется в
```
Зазвонил   д   н к — и начался д    н к.
Настоящий   д  н к должен быть с   д нк  .
"Мой любимый раздел физики — конечно же,      д н   к !" — сказал    дн к.
Он меня не услышал, потому что засмотрелся на   д нк  на щеке прекрасной   д  нк .
Один из д   н   к нашёл в       дн к  большой   д   н    к и — вот д      н к! — срезал его.
```

Если в одном слове есть несколько подслов "днк", то можно оставить любое.
(Но полезно при этом понимать, какое именно подслово оставляет регулярное выражение и почему.)


## Задача 7 («Цензор»)

Мы живём (всегда жили?) в век цензуры.
Так, сигареты [замазываются](https://dtf.ru/u/3351-vadim-elistratov/987583-zagadochnoe-delo-o-zamazannoy-sigarete-v-chetvertoy-matrice),
мужские достоинства [вырезаются](https://www.polygon.com/23467043/black-panther-wakanda-forever-namor-bulge),
женские — [заменяются на фрукты](https://dtf.ru/games/869120-frukty-vmesto-zhenshchiny-blizzard-zamenila-dve-otkrovennyh-kartiny-v-world-of-warcraft),
гигантским плюшевым медведям [запрещают играть в бутылочку](https://www.mirf.ru/news/nikakih-fetishej-furri-i-upominanij-lyucifera-sozdatel-graviti-folz-o-rabote-s-disney),
а Джованни, возможно, [готовится принять солнечную ванну](https://www.vedomosti.ru/society/news/2022/11/24/951902-gosduma-prinyala-zakon-o-zaprete-lgbt) температурой 451&nbsp;°F...

Так не будем же отставать от "тренда"!
Напишите программу с регуляркой, которая бы прятала (забивала звёздочками) "сомнительные" выражения в тексте.

Например, вход:
```
— Вот как... вы сопротивляетесь! — воскликнул де Жюссак.
— Тысяча чертей! Вас это удивляет?

— Дурак! Подпись: Oberst Schroder, скотина! Есть? Повтори!
— Oberst Schroder, скотина...
— Наконец-то, дубина! Кто принял телефонограмму?
— Я.
— Himmelherrgott! Кто это — «я»?
— Швейк. Что ещё?

Вино хлынуло, растекаясь по площади.
Смеющиеся уроды кинулись к ручейкам, опустились на четвереньки.
```

(*Oberst Schroder* — Полковник Шрёдер (нем.), *Himmelherrgott* — А, чтобы тебя чёрт подрал! (нем.))

Выход:
```
— Вот как... вы сопротивляетесь! — воскликнул де Жюссак.
— Тысяча ч****й! Вас это удивляет?

— Д***к! Подпись: Oberst Schroder, с*****а! Есть? Повтори!
— Oberst Schroder, с*****а...
— Наконец-то, дубина! Кто принял телефонограмму?
— Я.
— Himmelherrgott! Кто это — «я»?
— Швейк. Что ещё?

Вино хлынуло, растекаясь по площади.
Смеющиеся у***ы кинулись к ручейкам, опустились на четвереньки.
```


## Задача 8 («Chamomile Field»)

Замените с помощью регулярок в тексте все "ромашки" на "стекляшки".

Вход:
```
Ромашковое поле

Солнышко светит,
И я иду.
Куда — сама не знаю.
Чего-то жду.

И вот, за поворотом —
Огонь в глаза:
Ромашковое поле,
Без края и конца...

Боюсь шагнуть —
Вдруг обожгусь?
Боюсь зайти —
Вдруг не вернусь?

...Вернусь — куда?
Туда, где пусто.
Туда, где лишь ждала всегда
Того, кто б тоже ждал.

Пускай ж меня проглотит!
Это поле,
Поле из ромашек.
Пускай я утону!
И в нём ромашек,
Ромашек станет больше — на одну...

Вокруг — осколки солнца,
И я иду.
Куда, зачем — не знаю.
И ничего не жду.
```

Выход:
```
Стекляшковое поле

Солнышко светит,
И я иду.
Куда — сама не знаю.
Чего-то жду.

И вот, за поворотом —
Огонь в глаза:
Стекляшковое поле,
Без края и конца...

Боюсь шагнуть —
Вдруг обожгусь?
Боюсь зайти —
Вдруг не вернусь?

...Вернусь — куда?
Туда, где пусто.
Туда, где лишь ждала всегда
Того, кто б тоже ждал.

Пускай ж меня проглотит!
Это поле,
Поле из стекляшек.
Пускай я утону!
И в нём стекляшек,
Стекляшек станет больше — на одну...

Вокруг — осколки солнца,
И я иду.
Куда, зачем — не знаю.
И ничего не жду.
```


## Задача 9 («ПовестОчка»)

Регулярные выражения — очень полезный инструмент!
Мы уже убедились, что их можно использовать для *скрытия* "вредной" информации ("цензор").
Но ведь... этого мало?
Мало лишь скрыть ненужное.
Намного лучше было бы из ненужного сделать нужное — *изменить* существующую информацию.
Регулярки — довольно мощный инструмент по анализу строк.
Раскроем же их возможности более полно!

В настоящее время в некоторых кругах имеет популярность идея *расового разнообразия* (и вообще "разнообразия" в более широком смысле).
Это когда, например, в фильмах среди исполнителей ролей [обязательно должна быть некоторая доля людей – представителей "недопредставленных рас" (underrepresented racial groups)](https://www.theguardian.com/film/2020/sep/09/oscars-diversity-rules-hollywood).

Так давайте тоже быть "в тренде"!
Напишите программу с использованием регулярных варажений, которая бы делала "более разнообразным" подаваемый на вход текст.
(Не таким "white as hell", как [говорят люди, которые по данному вопросу находятся "на переднем крае"](https://twitter.com/SimuLiu/status/1595126266780274688).)

Итак, вход (нужные слова для наглядности выделены с двух сторон в звёздочки):
```
– Доброе утро, мистер Эллсворти.
Это был весьма изящный молодой человек, облачённый в красновато-коричневый костюм из грубой ткани.
Его отличали продолговатое **бледное** лицо, женский маленький рот, длинные чёрные волосы и жеманная походка.

Будь здесь Джулиана, она окрутила бы Чилдэна в полминуты.
Она такая соблазнительная, бойкая на язык, а главное – она женщина.
... Чилдэн просто упал бы в обморок при виде её чёрных волос, **бледной** кожи, меланхоличного, скучающего взгляда, безупречной груди, чуть туже, чем следует, обтянутой джемпером, в вырезе которого поблескивает серебро...

...После двух часов пути пришли к большому озеру.
— Нам тут не перейти, — сказал Гензель, — не вижу я ни жердинки, ни мосточка.
— И кораблика никакого нет, — сказала сестричка. — А зато вон там плавает **белая** уточка. Коли я её попрошу, она, конечно, поможет нам переправиться...
```

Выход:
```
– Доброе утро, мистер Эллсворти.
Это был весьма изящный молодой человек, облачённый в красновато-коричневый костюм из грубой ткани.
Его отличали продолговатое **тёмное** лицо, женский маленький рот, длинные чёрные волосы и жеманная походка.

Будь здесь Джулиана, она окрутила бы Чилдэна в полминуты.
Она такая соблазнительная, бойкая на язык, а главное – она женщина.
... Чилдэн просто упал бы в обморок при виде её чёрных волос, **тёмной** кожи, меланхоличного, скучающего взгляда, безупречной груди, чуть туже, чем следует, обтянутой джемпером, в вырезе которого поблескивает серебро...

...После двух часов пути пришли к большому озеру.
— Нам тут не перейти, — сказал Гензель, — не вижу я ни жердинки, ни мосточка.
— И кораблика никакого нет, — сказала сестричка. — А зато вон там плавает **чёрная** уточка. Коли я её попрошу, она, конечно, поможет нам переправиться...
```


# P.S.

При решении задач достаточно, чтобы программа корректно работала только на приведённом примере.
Но это не значит, что можно в код программы просто взять и "зашить" текст примера! :)

# P.P.S.

В [лабе про регулярки](http://cs.mipt.ru/advanced_python/lessons/lab12.html) много несложных (и не только несложных) упражнений.
Рекомендуется их дорешать ко конца!

# Ссылки

* [re](https://docs.python.org/3/library/re.html) — документация по билиотке `re` Питона
* [regex101.com](https://regex101.com/) — сайт, где можно поиграться с регулярными выражениями

## Отрывки из книг

* «Три мушкетёра», Александр Дюма
* «Похождения бравого солдата Швейка», Ярослав Гашек
* «Дочь железного дракона», Майкл Суэнвик
* «Убить легко», Агата Кристи
* «Человек в высоком замке», Филип Киндред Дик
* «Гензель и Гретель», Братья Гримм