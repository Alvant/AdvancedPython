"""A useless example of applying threads to a CPU bound problem
"""
import concurrent.futures
import time

from typing import List

from constants import CPU_BIG_NUMBERS
from utils import show_execution_time


def cpu_bound(number: int) -> int:
    return sum(i * i for i in range(number))


def find_sums(numbers: List[int], max_workers: int = 5) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(cpu_bound, numbers)


if __name__ == "__main__":
    show_execution_time(func=lambda: find_sums(CPU_BIG_NUMBERS))
