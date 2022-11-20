"""A useless example of applying asyncio to a CPU bound problem
"""
import asyncio
import time

from typing import Awaitable, List

from constants import CPU_BIG_NUMBERS
from utils import show_execution_time


async def cpu_bound(number: int) -> Awaitable[int]:
    return sum(i * i for i in range(number))


async def find_sums(numbers: List[int]) -> Awaitable[None]:
    tasks = list()
    
    for number in numbers:
        task = asyncio.ensure_future(cpu_bound(number))
        tasks.append(task)
     
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    show_execution_time(
        func=lambda: loop.run_until_complete(find_sums(CPU_BIG_NUMBERS)),
    )

    loop.close()
