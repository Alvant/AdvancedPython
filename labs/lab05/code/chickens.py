from enum import (
    IntEnum,
    auto,
)


class Character(IntEnum):
    INDIFFERENT = auto()
    CALM = auto()
    UNGOVERNABLE = auto()


class Chicken:
    pass  # TODO


class Egg(Chicken):
    _MAX_WEIGHT = 75
    _MAX_HEIGHT = 6

    def __init__(self, weight: float, height: float):
        super().__init__(
            weight=weight,
            height=height,
            character=Character.INDIFFERENT,
        )

    def eat(self, meal: float) -> None:
        self._weight = min(
            self._weight + meal / 2,
            self._MAX_WEIGHT,
        )
        self._height = min(
            self._height + meal / 2,
            self._MAX_HEIGHT,
        )

    def voice(self) -> str:
        return "Knock-Knock!"


class Cock(Chicken):
    def __init__(self, weight: float, height: float):
        super().__init__(
            weight=weight,
            height=height,
            character=Character.UNGOVERNABLE,
        )

    def voice(self) -> str:
        return "Cock-A-Doodle-Do!"

    def fight(self, other: 'Cock') -> None:
        self._weight = self._weight / 2
        other._weight = other._weight / 2


if __name__ == '__main__':
    chicken = Chicken(weight=1000, height=50)
    egg = Egg(weight=10, height=2)
    cock = Cock(weight=2000, height=90)

    creatures = [chicken, egg, cock]


    print('CREATURES')

    print('\nOne by one:')

    for creature in creatures:
        print(creature)

    print(f'\nAs a list: {creatures}')


    meal = 217.5

    print(f'\nFEEDING {meal}\n')

    for creature in creatures:
        creature.eat(meal)

    for creature in creatures:
        print(creature)


    print('\nVOICES\n')

    for creature in [chicken, egg, cock]:
        print(f'{creature.__class__.__name__}: {creature.voice()}')


    print('\nFIGHTING\n')

    try:
        egg.fight(cock)
    except AttributeError as error:
        print(f'Egg cannot fight: {str(error)}!')

    cock2 = Cock(weight=1500, height=100)

    print(f'Opponent cock: {cock2}')

    cock.fight(cock2)

    print(f'First cock after fight: {cock}')
    print(f'Second cock after fight: {cock2}')
