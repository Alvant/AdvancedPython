import time

from typing import List

from constants import CPU_BIG_NUMBERS
from utils import show_execution_time


def cpu_bound(number: int) -> int:
    return sum(i * i for i in range(number))


def find_sums(numbers: List[int]) -> None:
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    show_execution_time(func=lambda: find_sums(CPU_BIG_NUMBERS))
