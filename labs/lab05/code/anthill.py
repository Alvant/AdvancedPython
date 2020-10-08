import time

from collections import Counter

import numpy as np


class Anthill:
    def __init__(self, food: float):
        self._food = food
        self._ants = list()

    # TODO


class Ant:
    def __init__(
            self,
            required_food: float,
            death_probability: float,
            ):

        pass  # TODO

    def work(self):
        raise NotImplementedError()

    def is_alive(self):
        pass  # TODO


class Queen(Ant):
    def __init__(
            self,
            ant_classes: list,
            required_food: float = 1000,
            death_probability: float = 0.0001,
            max_num_ants: int = 100,
            ):
        super().__init__(
            required_food=required_food,
            death_probability=death_probability,
        )

        self._ant_classes = ant_classes
        self._max_num_ants = max_num_ants

    # TODO


class Worker(Ant):
    def __init__(
            self,
            required_food: int = 200,
            death_probability: float = 0.2,
            brought_food: int = 1000,
            ):

        pass  # TODO


class Soldier(Ant):
    def __init__(
            self,
            required_food: int = 500,
            death_probability: float = 0.7,
            ):

        pass  # TODO


class Fate:
    @classmethod
    def touch(cls, ant: Ant):
        pass  # TODO


if __name__ == '__main__':
    anthill = Anthill(food=2000)

    queen = Queen(ant_classes=[Worker, Soldier])
    anthill.accept(queen)

    num_workers = 150
    num_soldiers = 50

    for i in range(num_workers):
        anthill.accept(Worker())

    for i in range(num_soldiers):
        anthill.accept(Soldier())

    current_day = 1

    while len(anthill.ants) > 0 and anthill.food > 0:
        print(f'Day #{current_day}')
        print(f'{anthill.info()}\n')

        for ant in anthill.ants:
            ant.work()
            Fate.touch(ant)

        time.sleep(1)

        current_day += 1
